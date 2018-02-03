import struct
from bp import *
from datetime import datetime


# base loader class
class Loader:
    def __init__(self, path, count):
        """
        initiate loader
        :param path: data file path
        :param count: sample count in data file
        """
        self.path = path
        self.count = count
    
    def get_file_content(self):
        """
        get file content
        :return:
        """
        f = open(self.path, 'rb')
        content = f.read()
        f.close()
        return content
    
    def to_int(self, byte):
        """
        transfer unsigned byte to integer
        :param byte:
        :return:
        """
        return struct.unpack('B', byte)[0]


# image data loader
class ImageLoader(Loader):
    def get_picture(self, content, index):
        """
        internal function, get image from file
        :param content:
        :param index:
        :return:
        """
        start = index * 28 * 28 + 16
        picture = []
        for i in range(28):
            picture.append([])
            for j in range(28):
                picture[i].append(content[start + i * 28 + j])
        return picture
    
    def get_one_sample(self, picture):
        """
        internal function
        tranfer image to input vector of sample
        :param picture:
        :return:
        """
        sample = []
        for i in range(28):
            for j in range(28):
                sample.append(picture[i][j])
        return sample
    
    def load(self):
        """
        load data file, get input vectors of all samples
        :return:
        """
        content = self.get_file_content()
        data_set = []
        for index in range(self.count):
            data_set.append(self.get_one_sample(self.get_picture(content,
                                                                 index)))
        return data_set

    
# label data loader
class LabelLoader(Loader):
    def load(self):
        """
        load data file, get label vector of all samples
        :return:
        """
        content = self.get_file_content()
        labels = []
        for index in range(self.count):
            labels.append(self.norm(content[index + 8]))
        return labels
    
    def norm(self, label):
        """
        internal function
        transfer a value to ten-dimension vector
        :param label:
        :return:
        """
        label_vec = []
        label_value = label
        for i in range(10):
            if i == label_value:
                label_vec.append(0.9)
            else:
                label_vec.append(0.1)
        return label_vec

    
def get_training_data_set():
    """
    get training data set
    :return:
    """
    image_loader = ImageLoader('train-images.idx3-ubyte', 60000)
    label_loader = LabelLoader('train-labels.idx1-ubyte', 60000)
    return image_loader.load(), label_loader.load()


def get_test_data_set():
    """
    get test data set
    :return:
    """
    image_loader = ImageLoader('t10k-images.idx3-ubyte', 10000)
    label_loader = LabelLoader('t10k-labels.idx1-ubyte', 10000)
    return image_loader.load(), label_loader.load()


def get_result(vec):
    max_value_index = 0
    max_value = 0
    for i in range(len(vec)):
        if vec[i] > max_value:
            max_value = vec[i]
            max_value_index = i
    return max_value_index


def evaluate(network, test_data_set, test_labels):
    error = 0
    total = len(test_data_set)
    
    for i in range(total):
        label = get_result(test_labels[i])
        predict = get_result(network.predict(test_data_set[i]))
        if label != predict:
            error += 1
    return float(error) / float(total)


def train_and_evaluate():
    last_error_ratio = 1.0
    epoch = 0
    train_data_set, train_labels = get_training_data_set()
    test_data_set, test_labels = get_test_data_set()
    network = Network([784, 300, 10])
    while True:
        epoch += 1
        print('%s epoch %d begin' % (datetime.now(), epoch))
        network.train(train_labels, train_data_set, 0.3, 1)
        print('%s epoch %d finished' % (datetime.now(), epoch))
        if epoch % 10 == 0:
            error_ratio = evaluate(network, test_data_set, test_labels)
            print('%s after epoch %d, error ratio is %f' % (datetime.now(),
                                                            epoch, error_ratio))
            if error_ratio > last_error_ratio:
                break
            else:
                last_error_ratio = error_ratio


if __name__ == '__main__':
    train_and_evaluate()
