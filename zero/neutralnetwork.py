from functools import reduce
import random
import math


class Node:
    def __init__(self, layer_index, node_index):
        """
        construct node object
        :param layer_index: node's layer index
        :param node_index: node index
        """
        self.layer_index = layer_index
        self.node_index = node_index
        self.downstream = []
        self.upstream = []
        self.output = 0
        self.delta = 0
        
    def set_output(self, output):
        """
        setup output of the node. The function will be used if the node is
        in input layer
        :param output:
        :return:
        """
        self.output = output
    
    def append_downstream_connection(self, conn):
        """
        add a connection to downstream node
        :param conn:
        :return:
        """
        self.downstream.append(conn)
    
    def append_upstream_connection(self, conn):
        """
        add a connection to upstream node
        :param conn:
        :return:
        """
        self.upstream.append(conn)
    
    def calc_output(self):
        """
        :return: output of the node
        """
        output = reduce(lambda ret, conn: ret + conn.upstream_node.output *
                                          conn.weight, self.upstream, 0)
        self.output = sigmoid(output)
    
    def calc_hidden_layer_delta(self):
        """
        calculate delta when node is in hidden layer
        :return:
        """
        downstream_delta = reduce(lambda ret, conn: ret +
                  conn.downstream_node.output * conn.weight, self.downstream,
                                  0.0)
        self.delta = self.output * (1-self.output) * downstream_delta
    
    def calc_output_layer_delta(self, label):
        """
        calculate delta when node in output layer
        :param label:
        :return:
        """
        self.delta = self.output * (1 - self.output) * (label - self.output)
        
    def __str__(self):
        """
        print node information
        :return:
        """
        node_str = '%u-%u: output: 1' % (self.layer_index, self.node_index)
        downstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn),
                                self.downstream, '')
        return node_str + '\n\tdownstream:' + downstream_str
    

class ConstNode:
    def __init__(self, layer_index, node_index):
        """
        construct node object
        :param layer_index: layer index
        :param node_index: node index
        """
        self.layer_index = layer_index
        self.node_index = node_index
        self.downstream = []
        self.output = 1
        self.delta = 0
    
    def append_downstream_connection(self, conn):
        """
        append a connection to downstream
        :param conn:
        :return:
        """
        self.downstream.append(conn)
    
    def calc_hidden_layer_delta(self):
        """
        calculate delta of hidden layer
        :return:
        """
        downstream_delta = reduce(
                lambda ret, conn: ret + conn.downstream_node.delta*conn.weight,
                self.downstream, 0.0)
        self.delta = self.output * (1-self.output) * downstream_delta
        
    def __str__(self):
        """
        print node information
        :return:
        """
        node_str = '%u-%u: output: 1' % (self.layer_index, self.node_index)
        downstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn),
                                self.downstream, '')
        return node_str + '\n\tdownstream:' + downstream_str


class Layer:
    def __init__(self, layer_index, node_count):
        """
        initiate a lyer
        :param layer_index: layer index
        :param node_count: node number in the layer
        """
        self.layer_index = layer_index
        self.nodes = []
        for i in range(node_count):
            self.nodes.append(Node(layer_index, i))
        self.nodes.append(ConstNode(layer_index, node_count))
    
    def set_output(self, data):
        """
        setup layer output, used when the layer is input layer
        :param data:
        :return:
        """
        for i in range(len(data)):
            self.nodes[i].set_output(data[i])
    
    def calc_output(self):
        """
        calculate output vector of the layer
        :return:
        """
        for node in self.nodes[:-1]:
            node.calc_output()
        
    def dump(self):
        """
        print layer information
        :return:
        """
        for node in self.nodes:
            print(node)


class Connection:
    def __init__(self, upstream_node, downstream_node):
        """
        initiate connection, initial weight is a small random number
        :param upstream_node: upsteam node
        :param downstream_node: downstream node
        """
        self.upstream_node = upstream_node
        self.downstream_node = downstream_node
        self.weight = random.uniform(-0.1, 0.1)
        self.gradient = 0.0
    
    def cal_gradient(self):
        """
        calculate gradient
        :return:
        """
        self.gradient = self.downstream_node.delta * self.upstream_node.output
    
    def get_gradient(self):
        """
        get current gradient
        :return:
        """
        return self.gradient
    
    def update_weight(self, rate):
        """
        update weight according to gradient downward algorithm
        :param rate:
        :return:
        """
        self.cal_gradient()
        self.weight += rate * self.gradient
    
    def __str__(self):
        """
        print connection information
        :return:
        """
        return '(%u-%u) -> (%u-%u) = %f' % (
            self.upstream_node.layer_index,
            self.upstream_node.node_index,
            self.downstream_node.layer_index,
            self.downstream_node.node_index,
            self.weight
        )


class Connections:
    def __init__(self):
        self.connections = []
    
    def add_connection(self, connection):
        self.connections.append(connection)
        
    def dump(self):
        for conn in self.connections:
            print(conn)


class Network:
    def __init__(self, layers):
        """
        initiate a all connected neutral network
        :param layers: two-dimension list, describe nodes number of each layer
        """
        self.connections = Connections()
        self.layers = []
        layer_count = len(layers)
        node_count = 0
        for i in range(layer_count):
            self.layers.append(Layer(i, layers[i]))
        for layer in range(layer_count - 1):
            connections = [Connection(upstream_node, downstream_node)
                           for upstream_node in self.layers[layer].nodes
                           for downstream_node in self.layers[
                                                      layer+1].nodes[:-1]]
            for conn in connections:
                self.connections.add_connection(conn)
                conn.downstream_node.append_upstream_connection(conn)
                conn.upstream_node.append_downstream_connection(conn)
        
    def train(self, labels, data_set, rate, iteration):
        """
        train network
        :param labels: list, label of training data. each element is a label
                       of a sample
        :param data_set: character of training sample.
        :param rate:
        :param iteration:
        :return:
        """
        for i in range(iteration):
            for d in range(len(data_set)):
                self.train_one_sample(labels[d], data_set[d], rate)
    
    def train_one_sample(self, label, sample, rate):
        """
        internal function, train network via a sample
        :param label:
        :param sample:
        :param rate:
        :return:
        """
        self.predict(sample)
        self.calc_delta(label)
        self.update_weight(rate)
 #       self.dump()
        
    def calc_delta(self, label):
        """
        internal function, calculate delta of each node
        :param label:
        :return:
        """
        output_nodes = self.layers[-1].nodes
        for i in range(len(label)):
            output_nodes[i].calc_output_layer_delta(label[i])
        for layer in self.layers[-2::-1]:
            for node in layer.nodes:
                node.calc_hidden_layer_delta()
    
    def update_weight(self, rate):
        """
        internal function. update the weights
        :return:
        """
        for layer in self.layers[:-1]:
            for node in layer.nodes:
                for conn in node.downstream:
                    conn.update_weight(rate)
    
    def calc_gradient(self):
        """
        internal function, calculate gradient of every connection
        :return:
        """
        for layer in self.layers[:-1]:
            for node in layer.nodes:
                for conn in node.downstream:
                    conn.calc_gradient()
    
    def get_gradient(self, label, sample):
        """
        get gradient in every connection under one sample
        :param label:
        :param sample:
        :return:
        """
        self.predict(sample)
        self.calc_delta(label)
        self.calc_gradient()
        
    def predict(self, sample):
        """
        predict output according to input sample
        :param sample: list, sample feature, input vector
        :return:
        """
        self.layers[0].set_output(sample)
        for i in range(1, len(self.layers)):
            self.layers[i].calc_output()
        return list(map(lambda node: node.output, self.layers[-1].nodes[:-1]))
    
    def dump(self):
        """
        print network information
        :return:
        """
        for layer in self.layers:
            layer.dump()


def gradien_check(network, sample_feature, sample_label):
    """
    gradient check
    :param network: neutral network object
    :param sample_feature: feature of sample
    :param sample_label: label of sample
    :return:
    """
    # calculate network error
    def network_error(vec1, vec2):
        return 0.5 * reduce(lambda a, b: a + b, list(map(lambda v: (v[0]-v[
            1]) *
                    (v[0]-v[1]), zip(vec1, vec2))))
    # get gradient of every connection of current sample in the network
    network.get_gradient(sample_feature, sample_label)
    # check every gradient
    for conn in network.connections.connections:
        # get assigned gradient
        actual_gradient = conn.get_gradient()
        
        # increase a small value, calculate network error
        epsilon = 0.0001
        conn.weight += epsilon
        error1 = network_error(network.predict(sample_feature), sample_label)
        
        # substract a small value, calculate network error
        conn.weight -= 2 * epsilon
        error2 = network_error(network.predict(sample_feature), sample_label)
        
        # calculate expected gradient
        expected_gradient = (error2 - error1) / (2 * epsilon)
        
        # print
        print('expected gradient: \t%f\nactual gradient:\t\%f' %
              (expected_gradient, actual_gradient))


def sigmoid(x):
    try:
        return 1 / (1 + math.exp(-x))
    except:
        return 0
