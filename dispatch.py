
确定目标：
	（1）出现了未open的 type时候，当该type在scrollview的可视范围内，则播放特效
	（2）当category所有的 type都open了，那么取消这个category上的“新”

问题：
	（1）3秒回调，3秒过后，对象消失了（item被收回等等）--> 会发生什么？（1.None返回，因为TImer检测了，2.报错误，released）
	（2）

查看：
	（1）Timer

方案：
class Main()
	触发ItemPosChanged
	监听ItemPosChanged，Scrolling
		对每个在可视范围内的item，触发显示动态效果
	

class Category()


小结：
目前遇到的code：
	处理文件的脚本，解析excel，重构成字典

	我的计划是：找一篇入门指导，按照去做
	what is your 