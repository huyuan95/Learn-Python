import numpy as np
from activators import ReluActivator

class ConvLayer:
    def __init__(self, input_width, input_height, channel_number,
                 filter_width, filter_height, filter_number, zero_padding,
                 stride, activator, learning_rate):
        self.input_width = input_width
        self.input_height = input_height
        self.channel_number = channel_number
        self.filter_width = filter_width
        self.filter_height = filter_height
        self.filter_number = filter_number
        self.zero_padding = zero_padding
        self.stride = stride
        self.output_width = ConvLayer.calculate_output_size(
                self.input_width, self.input_height, zero_padding, stride
        )
        self.output_height = ConvLayer.calculate_output_size(
                self.input_height, self.filter_height, zero_padding, stride
        )
        self.output_array = np.zeros((self.filter_number, self.output_height,
                                      self.output_width))
        self.filters = []
        for i in range(filter_number):
            self.filters.append(Filter(filter_width, filter_height,
                                       self.channel_number))
        self.activator = activator
        self.learning_rate = learning_rate
    
    @staticmethod
    def calculate_output_size(input_size, filter_size, zero_padding, stride):
        return (input_size - filter_size + 2*zero_padding) / stride + 1
    
    def forward(self, input_array):
        """
        计算卷积层的输出，结果保存在self.output_array
        :param input_array:
        :return:
        """
        self.input_array = input_array
        self.padded_input_array = padding(input_array, self.zero_padding)
        for f in range(self.filter_number):
            filter = self.filters[f]
            conv(self.padded_input_array, filter.get_weights(),
                 self.output_array[f], self.stride, filter.get_bias[])
            element_wise_op(self.output_array, self.activator.forward)
        
    def bp_sensitivity_map(self, sensitivity_array, activator):
        """
        计算传递到上一层的sensitivity map
        :param sensitivity_array: 本层的sensitivity map
        :param activator: 激活函数
        :return:
        """
        # 处理卷积步长，对原始sensitivity map进行扩展
        expanded_array = self.expended_sensitivity_map(
                sensitivity_array
        )
        # full卷积，对sensitivity map进行扩展
        # 虽然原始输入的zero padding单元也会获得残差
        # 但这个残差不需要继续向上传递，因此就不计算了
        expanded_width = expanded_array.shape[2]
        zp = (self.input_width + self.filter_width - 1 - expanded_width) / 2
        
    
    
class Filter:
    def __init__(self, width, height, depth):
        self.weights = np.random.uniform(-1e-4, -1e-4, (depth, height, width))
        self.bias = 0
        self.weights_grad = np.zeros(self.weights.shape)
        self.bias_grad = 0
        
    def __repr__(self):
        return self.weights
    
    def get_bias(self):
        return self.bias
    
    def get_weights(self):
        return self.weights
    
    def update(self, learning_rate):
        self.weights -= learning_rate * self.weights_grad
        self.bias -= learning_rate * self.bias_grad
    
# 对numpy数组进行element wise操作
def element_wise_op(array, op):
    for i in np.nditer(array, op_flags = ['readwrite']):
        i[...] = op(i)

def conv(input_array,
         kernel_array,
         output_array,
         stride, bias):
    """
    计算卷积，自动适配输入为2D和3D的情况
    :param input_array:
    :param kernel_array:
    :param output_array:
    :param stride:
    :param bias:
    :return:
    """
    channel_number = input_array.ndim
    output_width = output_array.shape[1]
    output_height = output_array.shape[0]
    kernel_width = kernel_array.shape[-1]
    kernel_height = kernel_array.shape[-2]
    for i in range(output_height):
        for j in range(output_width):
            output_array[i][j] = (
                get_patch(input_array, i, j, kernel_width, kernel_height,
                          stride) * kernel_array
            ).sum() + bias
    
# 为数组增加zero padding操作
def padding(input_array, zp):
    """
    为数组增加zero padding， 自动适配输入为2D和3D的情况
    :param input_array:
    :param zp:
    :return:
    """
    if zp == 0:
        return input_array
    else:
        if input_array.ndim == 3:
            input_width = input_array.shape[2]
            input_height = input_array.shape[1]
            input_depth = input_array.shape[0]
            padded_array = np.zeros((
                input_depth,
                input_height + 2*zp,
                input_width + 2*zp
            ))
            padded_array[:, zp: zp + input_height, zp: zp + input_width] = \
                input_array
            return padded_array
        elif input_array.ndim == 2:
            input_width = input_array.shape[1]
            input_height = input_array.shape[0]
            padded_array = np.zeros((
                input_height + 2*zp,
                input_width + 2*zp
            ))
            padded_array[zp: zp + input_height, zp: zp + input_width] = \
                input_array
            return padded_array
    
