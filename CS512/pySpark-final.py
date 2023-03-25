### gs://cs-512/pySpark-final.py
### gs://hadoop-lib/bigquery/bigquery-connector-hadoop2-latest.jar

## gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar

import pyspark
import pprint

from pyspark.sql.types import MapType,StringType, IntegerType
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, explode
from google.cloud import storage
from py4j.protocol import Py4JJavaError


# Define commonly used male & female matching words
male_words = ['guy','spokesman','chairman',"mens",'men','him',"hes",'his','boy','boyfriend','boyfriends','boys','brother','brothers','dad','dads','dude','father','fathers','fiance','gentleman','gentlemen','god','grandfather','grandpa','grandson','groom','he','himself','husband','husbands','king','male','man','mr','nephew','nephews','priest','prince','son','sons','uncle','uncles','waiter','widower','widowers', 'waiter']

female_words = ['heroine','spokeswoman','chairwoman',"womens",'actress','women',"shes",'her','aunt','aunts','bride','daughter','daughters','female','fiancee','girl','girlfriend','girlfriends','girls','goddess','granddaughter','grandma','grandmother','herself','ladies','lady','lady','mom','moms','mother','mothers','mrs','ms','niece','nieces','priestess','princess','queens','she','sister','sisters','waitress','widow','widows','wife','wives','woman', 'waitress']

# aggregate the number of male and female matching words in each review
def count_gender(sentence_words):
    gender_count = dict()
    for word in sentence_words.split():
        if word in male_words:
            gender_count[word] = gender_count.get(word, 0) + 1
        elif word in female_words:
            gender_count[word] = gender_count.get(word, 0) + 1
        else:
            pass

    return gender_count

sc = pyspark.SparkContext()

bucket = sc._jsc.hadoopConfiguration().get('fs.gs.system.bucket')
project = sc._jsc.hadoopConfiguration().get('fs.gs.project.id')
input_directory = 'gs://{}/hadoop/tmp/bigquerry/pyspark_input'.format(bucket)
output_directory = 'gs://{}/pyspark_demo_output'.format(bucket)

# Define fully qualified table location
table = 'gh-bigq-bigd.yelp_reviews.yelp_reviews'

# create the space session
spark = SparkSession.builder.appName('reviews').getOrCreate()

# if no table tell me it doesn't exist
try:
    df = spark.read.format('bigquery').option('table', table).load()
except Py4JJavaError:
    print(f'{table} does not exist')

# create temp table to subset dataframes on stars
df.createOrReplaceTempView('df_temp')

# Subset for each review level I am interested id
df_1star = spark.sql(
    'SELECT text \
    FROM df_temp \
    WHERE review_stars = 1'
)

df_3star = spark.sql(
    'SELECT text \
    FROM df_temp \
    WHERE review_stars = 3'
)

df_5star = spark.sql(
    'SELECT text \
    FROM df_temp \
    WHERE review_stars = 5'
)

# create user defined function that returns the word and the count, as string and integer
word_counter = udf(count_gender, MapType(StringType(), IntegerType()))

# select a row and use the word counter on the exploded string (create a new 'row' for each thing in the array)
df_1star_count = df_1star.select(explode(word_counter('text')).alias('word', 'count'))
df_3star_count = df_3star.select(explode(word_counter('text')).alias('word', 'count'))
df_5star_count = df_5star.select(explode(word_counter('text')).alias('word', 'count'))

# aggregate, and sum
df_1star_agg = df_1star_count.groupBy('word').sum('count')
df_3star_agg = df_3star_count.groupBy('word').sum('count')
df_5star_agg = df_5star_count.groupBy('word').sum('count')

# show the top 40 from Descending order
df_1star_agg.orderBy('sum(count)', ascending = False).show(40)
df_3star_agg.orderBy('sum(count)', ascending = False).show(40)
df_5star_agg.orderBy('sum(count)', ascending = False).show(40)