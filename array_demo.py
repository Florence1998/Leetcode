class Array:  # 声明数组类
    def __init__(self, capacity) -> None:
        """
        初始化数组
        :param capacity: 数组的容量
        """
        # 数组需要一个地方data来存数据
        self.data = [-1] * capacity
        # count记录当前数组存了多少数据
        self.count = 0
        # n表示数组的容量，可以自定义
        self.n = capacity

    def insert(self, location, value):
        """
        数组的插入
        :param location: 插入的位置（索引）
        :param value: 插入的值
        :return:
        """
        if self.n == self.count:
            return False

        if location < 0 or location > self.count:
            return False

        for i in range(self.count, location, -1):
            self.data[i] = self.data[i - 1]

        self.data[location] = value
        self.count += 1
        return True

    def find(self, location):
        if location < 0 or location >= self.count:
            return -1

        return self.data[location]

    def delete(self, location):
        if location < 0 or location >= self.count:
            return False

        for i in range(location + 1, self.count):
            self.data[i - 1] = self.data[i]

        self.count -= 1
        return True


def test_demo():
    """简单的测试用例，都通过了，说明你数组的插入、删除、查找都没有问题"""
    array = Array(5)  # 创建了5个容量的数组
    array.insert(0, 1)
    array.insert(0, 2)
    array.insert(1, 3)
    array.insert(2, 4)
    array.insert(4, 5)

    # 判断插入不成功
    assert not array.insert(0, 100)
    assert array.find(0) == 2
    assert array.find(2) == 4
    assert array.find(4) == 5
    assert array.find(10) == -1
    assert array.count == 5
    removed = array.delete(4)
    assert removed
    assert array.find(4) == -1
    removed = array.delete(10)
    assert not removed
    # 2 3 4 1 5
    assert array.data == [2, 3, 4, 1, 5]


if __name__ == '__main__':
    test_demo()