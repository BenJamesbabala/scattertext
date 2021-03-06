from unittest import TestCase

from datashape import pprint

from scattertext.ChineseNLP import chinese_nlp


class TestChineseNLP(TestCase):
	def setUp(self):
		self.text = '''总理主持召开的这场座谈会，旨在听取专家学者和企业界人士对《政府工作报告（征求意见稿）》的意见建议。胡玮炜和另外6名不同专业、领域的专家、企业家受邀参加。\n李克强对胡玮炜的细致提问始终围绕虚拟经济和实体经济，以及新旧动能转换。他关心自行车制造材料，也询问所采用的互联网技术。 “摩拜单车听起来是经营方式的革命，但基础还是自行车，还是要靠实体经济支撑。反过来，实体经济也要靠服务变革来带动。”总理指出。\n当听到这家共享智能单车企业在不到一年的时间发展为拥有80万辆自行车的规模后，李克强充分肯定此类互联网企业对实体经济的带动作用，“某个自行车企业可能就被你带活了，新兴服务业的发展给制造业创造了巨大的市场空间”。\n相关资料显示，受益于共享单车，国内传统的自行车产业正在迎来春天，至少带动了160万辆以上自行车的制造生产。甚至有生产自行车零部件的上市公司因此股票涨停。美国彭博新闻社网站注意到这一现象，评价说“中国正重新成为自行车大国”。'''

	def test_main(self):
		doc = chinese_nlp(self.text)
		sent1 = doc.sents[0]
		self.assertEqual(str(sent1), '总理 主持 召开 的 这场 座谈会 ， 旨在 听取 专家学者 和 企业界 人士 对 《 政府 工作 报告 （ 征求意见 稿 ） 》 的 意见建议 。')
		self.assertEqual(len(doc.sents), 11)