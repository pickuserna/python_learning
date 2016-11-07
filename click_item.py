#this is test for git bound sublime
def click_category(self, index):
	#对于已经展开的list->收回list，设置category的高亮状态。 #并且如果该category是当前选中type的cate，那么取消type的选中状态
	item = self._listview_left.get_item_by_index(index)
	item.set_select(True)
	if self.click_category_index == index:
		if self.click_category_index == index:

	#对于没有展开的list,展开list，并将第一个type设置为选中状态



###明天的任务
def show_new_species_sigh(self):

（1）出现在屏幕内的item，设置其new 标记，并在3秒后失效
（2）当出现滑动的时候,有出现在scrollview的item，那么进入到状态机处理中

def is_in_the_scrollview(item):


def on_scrollview_scroll():
	#scrollview滑动的时候（on_scroll_end），如果有出现在view范围内的item，那么设置item的appear为true

##################
# 使用状态机完成
class state_machine():

class Normal():
	def __enter__():

	def __exit__():

class Appear():
	def __enter__():

	def __exit__():
