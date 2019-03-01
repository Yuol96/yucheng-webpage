import json

def genCourseraData():
	dct = {
		'Develop': [
			{
				'name': 'HTML, CSS, and Javascript for Web Developers',
				'certificate': 'https://www.coursera.org/account/accomplishments/certificate/CYZLFKN6FTFP',
				'link': 'https://www.coursera.org/learn/html-css-javascript-for-web-developers',
				'img': 'imgs/coursera/jhep-coursera-course4.jpeg',
				'university': "John Hopkins University",
				'specialization': False,
			},
			{
				'name': 'Concurrent Programming in Java',
				'certificate': 'https://www.coursera.org/account/accomplishments/certificate/QB77Z9N5NS7B',
				'link': 'https://www.coursera.org/learn/concurrent-programming-in-java',
				'img': 'imgs/coursera/concurrent.jpeg',
				'university': "Rice University",
				'specialization': False,
			},
		],
		'Machine Learning & Deep Learning': [
			{
				'name': 'Machine Learning',
				'certificate': 'https://www.coursera.org/account/accomplishments/specialization/certificate/78ACWG225K4F',
				'link': 'https://www.coursera.org/specializations/machine-learning',
				'img': 'imgs/coursera/machinelearning.jpeg',
				'specialization': True,
				'university': "Washington University",
				'courses': [
					{
						'name': 'Machine Learning Foundations: A Case Study Approach',
						'certificate': 'https://www.coursera.org/account/accomplishments/verify/6N9Q44KUHQW9',
					},
					{
						'name': 'Machine Learning: Regression',
						'certificate': 'https://www.coursera.org/account/accomplishments/certificate/RK6HF8G58QDX',
					},
					{
						'name': 'Machine Learning: Classification',
						'certificate': 'https://www.coursera.org/account/accomplishments/verify/PYEK24TJMY49',
					},
					{
						'name': 'Machine Learning: Clustering & Retrieval',
						'certificate': 'https://www.coursera.org/account/accomplishments/verify/5LHYMJJLLAE4',
					},
				]
			},
			{
				'name': 'Structuring Machine Learning Projects',
				'certificate': 'https://www.coursera.org/account/accomplishments/certificate/KPGAGAFYWGPM',
				'link': 'https://www.coursera.org/learn/machine-learning-projects',
				'img': 'imgs/coursera/CarouselAds_DL_ML.jpeg',
				'university': "deeplearning.ai",
				'specialization': False,
			},
			{
				'name': 'Improving Deep Neural Networks: Hyperparameter tuning, Regularization and Optimization',
				'certificate': 'https://www.coursera.org/account/accomplishments/verify/SVSUUCSYK6CM',
				'link': 'https://www.coursera.org/learn/deep-neural-network',
				'img': 'imgs/coursera/CarouselAds_DL_Tuning.jpeg',
				'university': "deeplearning.ai",
				'specialization': False,
			},
			{
				'name': 'Neural Networks and Deep Learning',
				'certificate': 'https://www.coursera.org/account/accomplishments/verify/ADWV3R3AW2BY',
				'link': 'https://www.coursera.org/learn/neural-networks-deep-learning',
				'img': 'imgs/coursera/CarouselAds_DL_Neural.jpeg',
				'university': "deeplearning.ai",
				'specialization': False,
			},
			{
				'name': 'Applied Machine Learning in Python',
				'certificate': 'https://www.coursera.org/account/accomplishments/certificate/8XRWSBU6XVH3',
				'link': 'https://www.coursera.org/learn/python-machine-learning',
				'img': 'imgs/coursera/python_datascience_thumbnail_machinelearning_1x1.jpeg',
				'university': "University of Michigan",
				'specialization': False,
			},

		],
		'Programming Languages & Data Structures and Algorithms': [
			{
				'name': 'Introduction to Scripting in Python',
				'certificate': 'https://www.coursera.org/account/accomplishments/specialization/certificate/DNGX8GPV9YYA',
				'link': 'https://www.coursera.org/specializations/introduction-scripting-in-python',
				'img': 'imgs/coursera/Python-Developer.jpeg',
				'university': "Rice University",
				'specialization': True,
				'courses': [
					{
						'name': 'Python Programming Essentials',
						'certificate': 'https://www.coursera.org/account/accomplishments/verify/3YKERP76G22W',
					},
					{
						'name': 'Python Data Representations',
						'certificate': 'https://www.coursera.org/account/accomplishments/verify/WGT94QAV6Q7Y',
					},
					{
						'name': 'Python Data Visualization',
						'certificate': 'https://www.coursera.org/account/accomplishments/verify/UPMRTDPJMGTX',
					},
					{
						'name': 'Python Data Analysis',
						'certificate': 'https://www.coursera.org/account/accomplishments/verify/QWCL5WF6JPLD',
					},
				],
			},
			{
				'name': 'Java Programming: Arrays, Lists, and Structured Data',
				'certificate': 'https://www.coursera.org/account/accomplishments/verify/6T23MRAV3UKV',
				'link': 'https://www.coursera.org/learn/java-programming-arrays-lists-data',
				'img': 'imgs/coursera/work-731198_1280.jpeg',
				'university': "Duke University",
				'specialization': False,
			},
			{
				'name': 'Java Programming: Solving Problems with Software',
				'certificate': 'https://www.coursera.org/account/accomplishments/verify/ZDBKB6R84J8R',
				'link': 'https://www.coursera.org/learn/java-programming',
				'img': 'imgs/coursera/Java.jpeg',
				'university': "Duke University",
				'specialization': False,
			},
			{
				'name': 'Data structures Basics',
				'certificate': 'https://www.coursera.org/account/accomplishments/verify/6UQDAY2WSSCZ',
				'link': 'https://www.coursera.org/learn/shuju-jiegou-suanfa',
				'img': 'imgs/coursera/sjjg_608x211_info.jpeg',
				'university': "Peking University",
				'specialization': False,
			},
			{
				'name': 'Advanced Data Structures and Algorithms',
				'certificate': 'https://www.coursera.org/account/accomplishments/verify/CEJYKXA6LPN9',
				'link': 'https://www.coursera.org/learn/gaoji-shuju-jiegou',
				'img': 'imgs/coursera/dsalgo2_logo_g.jpeg',
				'university': "Peking University",
				'specialization': False,
			},
			{
				'name': 'C++ Programming',
				'certificate': 'https://www.coursera.org/account/accomplishments/verify/CEG2ZPN7SMWQ',
				'link': 'https://www.coursera.org/learn/cpp-chengxu-sheji',
				'img': 'imgs/coursera/__logo2.jpeg',
				'university': "Peking University",
				'specialization': False,
			},
			{
				'name': 'Programming for Everybody (Getting Started with Python)',
				'certificate': 'https://www.coursera.org/account/accomplishments/verify/4RWHWQYZ5FTD',
				'link': 'https://www.coursera.org/learn/python',
				'img': 'imgs/coursera/pythonlearn_thumbnail_1x1.jpeg',
				'university': "University of Michigan",
				'specialization': False,
			},
			{
				'name': 'Python Data Structures',
				'certificate': 'https://www.coursera.org/account/accomplishments/verify/7K9QJMYT6U8K',
				'link': 'https://www.coursera.org/learn/python-data',
				'img': 'imgs/coursera/pythondata_thumbnail_1x1.jpeg',
				'university': "University of Michigan",
				'specialization': False,
			},
			{
				'name': 'Using Databases with Python',
				'certificate': 'https://www.coursera.org/account/accomplishments/verify/75V78SAT59A6',
				'link': 'https://www.coursera.org/learn/python-databases',
				'img': 'imgs/coursera/pythondatabases_thumbnail_1x1.jpeg',
				'university': "University of Michigan",
				'specialization': False,
			},
			{
				'name': 'Using Python to Access Web Data',
				'certificate': 'https://www.coursera.org/account/accomplishments/verify/S5XHVKSMNWC3',
				'link': 'https://www.coursera.org/learn/python-network-data',
				'img': 'imgs/coursera/pythonnetworkdata_thumbnail_1x1.jpeg',
				'university': "University of Michigan",
				'specialization': False,
			},
		],
		'Basics': [
			{
				'name': 'Operating Systems',
				'certificate': 'https://www.coursera.org/account/accomplishments/certificate/LEUMDCW6D2BY',
				'link': 'https://www.coursera.org/learn/os-pku',
				'img': 'imgs/coursera/os_pku.jpg',
				'university': "Peking University",
				'specialization': False,
			},
			{
				'name': 'The Unix Workbench',
				'certificate': 'https://www.coursera.org/account/accomplishments/certificate/8LV65K4JXYWN',
				'link': 'https://www.coursera.org/learn/unix',
				'img': 'imgs/coursera/cover_square.jpeg',
				'university': "John Hopkins University",
				'specialization': False,
			},
			{
				'name': 'Version Control with Git',
				'certificate': 'https://www.coursera.org/account/accomplishments/certificate/G6Z9FFYZTWXJ',
				'link': 'https://www.coursera.org/learn/version-control-with-git',
				'img': 'imgs/coursera/Course-1-Logo.jpeg',
				'university': "Atlassian",
				'specialization': False,
			},
			{
				'name': 'Introduction to MongoDB',
				'certificate': 'https://www.coursera.org/account/accomplishments/certificate/9SDK5VHMWUU5',
				'link': 'https://www.coursera.org/learn/introduction-mongodb',
				'img': 'imgs/coursera/logo-first-app-coursera.jpeg',
				'university': "MongoDB Inc.",
				'specialization': False,
			},

		],
	}
	jsonStr = json.dumps(dct)
	return jsonStr

def gen():
	with open('data/coursera.json', 'w') as hd:
		hd.write(genCourseraData())

if __name__ == '__main__':
	gen()

