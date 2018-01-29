from functools import reduce

class Perceptron():
    def __init__(self, input_num, activator):
        '''
        initiate perceptron
        :param input_num:number of inputs
        :param activator: activator funtion
        activator type: double->double
        '''
        self.activator = activator
        # initial weight vector is zero
        self.weights = [0.0 for _ in range(input_num)]
        # initial bias is zero
        self.bias = 0.0
        
    def __str__(self):
        '''
        print weights and bias after learning
        :return:
        '''
        return 'weights\t:%s\nbias\t:%f\n' % (self.weights, self.bias)
    
    def predict(self, input_vec):
        '''
        output calculated result of perceptron
        :param input_vec: input vector
        :return: calculated result of perceptron
        '''
        # pack input_vec[x1, x2, x3,...] and weights[w1, w2, w3,...]
        # to [(x1, w1), (x2, w2), (x3, w3),...]
        # calculate [x1*w1, x2*w2, x3*w3,...] by map function
        # sum up by reduce function
        return self.activator(
                reduce(lambda a, b: a+b,
                map(lambda x: x[0] * x[1], zip(input_vec, self.weights)), \
                0.0) + self.bias)
    
    def train(self, input_vecs, labels, iteration, rate):
        '''
        :param input_vec: training vector
        :param labels: labels for training vector
        :param iteration: train iteration
        :param rate: learn rate
        :return:
        '''
        for i in range(iteration):
            self._one_iteration(input_vecs, labels, rate)
    
    def _one_iteration(self, input_vecs, labels, rate):
        '''
        one iteration
        :param input_vec:
        :param labels:
        :param rate:
        :return:
        '''
        samples = zip(input_vecs, labels)
        for (input_vec, label) in samples:
            output = self.predict(input_vec)
            self._update_weights(input_vec, output, label, rate)
        
    def _update_weights(self, input_vec, output, label, rate):
        '''
        update perceptron weights
        :param input_vec:
        :param output:
        :param label:
        :param rate:
        :return:
        '''
        delta = label - output
        self.weights = list(map(
                lambda x: x[1] + rate*delta*x[0],
                zip(input_vec, self.weights)))
        self.bias += delta * rate
        

def f(x):
    '''
    acticator function
    :param x:
    :return:
    '''
    return 1 if x > 0 else 0

def get_training_dataset():
    '''
    config training dateset according to and truth value table
    :return:
    '''
    input_vecs = [[1,1], [0,0], [1,0], [0,1]]
    labels = [1, 0, 0, 0]
    return input_vecs, labels

def train_and_perceptron():
    '''
    train perceptron
    :return:
    '''
    p = Perceptron(2, f)
    input_vecs, labels = get_training_dataset()
    p.train(input_vecs, labels, 10, 0.1)
    return p

if __name__ == '__main__':
    and_perception = train_and_perceptron()
    print(and_perception)
    
    print('1 and 1 = %d' % and_perception.predict([1,1]))
    print('1 and 0 = %d' % and_perception.predict([1, 0]))
    print('0 and 0 = %d' % and_perception.predict([0, 0]))
    print('0 and 1 = %d' % and_perception.predict([0, 1]))
