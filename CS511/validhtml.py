import re


def valid_html(example_set):
	"""This function will take in a set of html code strings and return a boolean if the format is valid or not valid"""
	parsed = []    # empty list to be returned in format [('html', True or False), ..., ...] for how many ever strings were fed into the function

	for html in example_set:
		html_tag_dict = {}
		all_tags = re.findall('(\<\/\w{1,15}\>|\<\w{1,15}\>)', html)    # each loop this is a list of the tags and their order from html
		keys = re.findall('\<\\w{1,15}\>', html)   # list of the keys that belong to the html string keys are defined as closing tag </foo>

		for key in keys:
			value = '</' + key[1:]   # the value that belongs to the key i.e. if key </foo> then value <foo>
			html_tag_dict[key] = value  # create the dynamic dictionary

		check_tag = []

		for tag in all_tags:
			if tag in html_tag_dict.keys():
				check_tag.append(tag)
			elif not check_tag or len(all_tags) % 2 != 0:
				parsed.append((html, False))
				break
			elif tag != html_tag_dict[check_tag.pop()]:
				parsed.append((html, False))
				break
			elif not check_tag:
				parsed.append((html, True))

	return parsed

