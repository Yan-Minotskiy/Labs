import random
import skimage

# bipolar case
class HammingNeuron:

    def __init__(self, weights, next_neuron=None):
        self.weights = list()
        self.inputs = []
        self.next_neuron = None
        for w in weights:
            self.weights.append(w)
            self.inputs.append(0)
            self.next_neuron = next_neuron

    def change_weight(self, ind_of_weight, new_value):
        self.weights[ind_of_weight] = new_value

    def set_input(self, ind_of_input, value):
        self.inputs[ind_of_input] = value

    def set_next_neuron(self, next_neuron):
        self.next_neuron = next_neuron

    def count_output(self):
        return 1 / 2 + sum(
            self.inputs[i] * self.weights[i] for i in range(len(self.weights))
        ) / (2 * len(self.weights))

    def get_output(self):
        self.next_neuron.set_value(self.count_output())


class MaxNetNeuron:

    def __init__(self, index, weights, next_neuron):
        self.value = 0
        self.reinitial_value = 0
        self.inputs = []
        self.weights = []
        self.layer_neurons = list()
        self.index = index
        self.next_neuron = next_neuron
        for w in weights:
            self.weights.append(w)
            self.inputs.append(None)

    def set_layer_neurons(self, layer_neurons):
        for n in layer_neurons:
            self.layer_neurons.append(n)

    def set_value(self, value):
        self.value = value
        self.reinitial_value = value

    def set_only_current_value(self, value):
        self.value = value

    def set_input(self, ind_of_neuron, value):
        self.inputs[ind_of_neuron] = value

    def count_output(self):
        # if first time
        if self.inputs[self.index] is None:
            return self.value
        # if not first time
        else:
            return self.inputs[self.index] - \
                sum(self.inputs[i] * self.weights[i] for i in range(0, len(self.weights)) if i != self.index)

    def recount_value(self):
        self.value = self.count_output()

    def get_output_inside_layer(self):
        for n in self.layer_neurons:
            n.set_input(self.index, self.value)

    def get_output(self):
        self.next_neuron.set_value(self.value)

    def reinitialize_neuron(self):
        self.value = self.reinitial_value
        for i in range(len(self.inputs)):
            self.inputs[i] = None


class ThresholdNeuron:

    def __init__(self, index, next_neurons):
        self.value = None
        self.next_neurons = []
        self.index = index
        for n in next_neurons:
            self.next_neurons.append(n)

    def set_value(self, value):
        self.value = value

    def count_output(self):
        if self.value > 0:
            return 1
        else:
            return 0

    def get_output(self):
        for n in self.next_neurons:
            n.set_input(self.index, self.count_output())


class OutputNeuron:

    def __init__(self, weights):
        self.weights = list()
        self.inputs = []
        for w in weights:
            self.weights.append(w)
            self.inputs.append(0)

    def set_input(self, index, value):
        self.inputs[index] = value

    def get_output(self):
        jls_extract_var = sum
        return jls_extract_var(self.weights[i] * self.inputs[i] for i in range(len(self.weights)))


class HammingLayer:

    def __init__(self, weights, next_neurons):
        self.neurons = []
        for i in range(len(weights)):
            new_neuron = HammingNeuron(weights[i], next_neurons[i])
            self.neurons.append(new_neuron)

    def run(self, inputs):
        for n in self.neurons:
            for i in range(len(inputs)):
                n.set_input(i, inputs[i])
        for n in self.neurons:
            n.get_output()


class MaxNetLayer:

    def __init__(self, next_neurons):
        self.neurons = []
        k = len(next_neurons)
        for i in range(k):
            weights = (
                [random.random() * 1 / (k - 1) for j in range(i)]
                + [1]
                + [random.random() * 1 / (k - 1) for j in range(i + 1, k)]
            )

            new_neuron = MaxNetNeuron(i, weights, next_neurons[i])
            self.neurons.append(new_neuron)
        for n in self.neurons:
            n.set_layer_neurons(self.neurons)

    def run(self):
        for n in self.neurons:
            n.get_output_inside_layer()
        for n in self.neurons:
            n.recount_value()
        for n in self.neurons:
            n.get_output()

    def reinitialize_layer(self, num_of_not_null_neuron, eps):
        self.neurons[num_of_not_null_neuron].reinitial_value -= eps
        for n in self.neurons:
            n.reinitialize_neuron()


class ThresholdLayer:

    def __init__(self, count, next_neurons):
        self.neurons = []
        for i in range(count):
            new_neuron = ThresholdNeuron(i, next_neurons)
            self.neurons.append(new_neuron)

    def run(self):
        for n in self.neurons:
            n.get_output()

    def get_first_not_null_element(self):
        for n in self.neurons:
            if n.count_output() == 1:
                return self.neurons.index(n)


class OutputLayer:
    def __init__(self, weights):
        self.neurons = []
        for i in range(len(weights[0])):
            self.neurons.append(OutputNeuron([weights[j][i] for j in range(len(weights))]))

    def get_result(self):
        return [n.get_output() for n in self.neurons]


class HammingNetwork:
    """
    Initial arguments:
        learning_examples - list of learning examples
        eps - maximal distance between winners
        max_count_of_outputs - maximal count of winners
    """

    def __init__(self, learning_examples, eps, max_count_of_outputs):
        self.max_count_of_outputs = max_count_of_outputs
        self.eps = eps
        self.output_layer = OutputLayer(learning_examples)
        self.threshold_layer = ThresholdLayer(len(learning_examples), self.output_layer.neurons)
        self.max_net_layer = MaxNetLayer(self.threshold_layer.neurons)
        self.hamming_layer = HammingLayer(learning_examples, self.max_net_layer.neurons)

    def classification(self, example_inputs):
        res = []
        self.hamming_layer.run(example_inputs)
        first_time = True
        while(True):
            while(True):
                self.max_net_layer.run()
                if sum(n.count_output() for n in self.threshold_layer.neurons) == 1:
                    break
                for n in self.max_net_layer.neurons:
                    if n.next_neuron.count_output() == 0:
                        n.set_only_current_value(0)
            self.threshold_layer.run()
            res.append(self.output_layer.get_result())
            if first_time:
                first_time = False
                self.max_net_layer.reinitialize_layer(self.threshold_layer.get_first_not_null_element(), self.eps)
                continue
            else:
                if res[len(res) - 1] in res[0:len(res) - 1] or len(res) > self.max_count_of_outputs:
                    res = res[0:len(res) - 1]
                    return res
                else:
                    self.max_net_layer.reinitialize_layer(self.threshold_layer.get_first_not_null_element(), self.eps)
                    continue


if __name__ == '__main__':
    dict_of_numbers = {'0': [1, 1, 1, 
                             1, -1, 1,
                             1, -1, 1,
                             1, -1, 1, 
                             1, 1, 1],

                       '1': [-1, -1, 1,
                             -1, 1, 1,
                              1, -1, 1, 
                             -1, -1, 1,
                             -1, -1, 1],

                       '2': [1, 1, 1, 
                             1, -1, 1, 
                             -1, -1, 1, 
                             -1, 1, -1, 
                             1, 1, 1],

                       '3': [1, 1, 1, 
                             -1, -1, 1, 
                             -1, 1, 1, 
                             -1, -1, 1,
                             1, 1, 1], 

                       '4': [1, -1, 1, 
                             1, -1, 1, 
                             1, 1, 1, 
                             -1, -1, 1,
                             -1, -1, 1],
                             
                       '5': [1, 1, 1, 
                             1, -1, -1, 
                             1, 1, 1,
                             -1, -1, 1,
                             1, 1, 1],

                       '6': [1, 1, 1, 
                             1, -1, -1, 
                             1, 1, 1, 
                             1, -1, 1,
                             1, 1, 1], 
                             
                       '7': [1, 1, 1, 
                             -1, -1, 1,
                             -1, 1, -1,
                             1, -1, -1,
                             1, -1, -1],

                       '8': [1, 1, 1,
                             1, -1, 1,
                             -1, 1, -1,
                             1, -1, 1,
                             1, 1, 1,],

                       '9': [1, 1, 1,
                             1, -1, 1,
                             1, 1, 1,
                             -1, -1, 1,
                             1, 1, 1,]}

    my_learning_examples = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    my_validation_examples = ['0', '1', '5']
    my_eps = 0.3
    max_count_of_output = 1
    my_hamming_network = HammingNetwork([dict_of_numbers[k] for k in my_learning_examples], my_eps, max_count_of_output)
    for ex in my_validation_examples:
        print('example')
        print(str(ex))
        for ans in my_hamming_network.classification(dict_of_numbers[ex]):
            print('answer')
            print([key for key, val in list(dict_of_numbers.items()) if val == ans][0])
        print('-------------------------------------------')