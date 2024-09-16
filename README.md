# Artificial Intelligence and Machine Learning Final Assignment
![Convolutional Neural Network for Assignment](cnn.png)

The goal of this assignment was to implement a simple two-layer Convolutional Neural Network (CNN). As depicted in the image, the CNN has five inputs, _x_<sub>1</sub> to _x_<sub>5</sub>, four hidden nodes, _z_<sub>1</sub> to _z_<sub>4</sub>, and a single output node, _y_, and ReLU activations. The hidden layer and output of the CNN was to be computed alongside the gradient of the hidden layer and output w.r.t weight _w_<sub>1</sub>. We were given the value of the weights and these are _w_<sub>1</sub> = 1.2, _w_<sub>2</sub> = -0.2, _v_<sub>1</sub> = -0.3, _v_<sub>2</sub> = 0.6, _v_<sub>3</sub> = 1.3 and _v_<sub>4</sub> = -1.5.

The `convnet()` function takes a single argument, x, a list of five numerical inputs. These inputs need to be converted to the dual type. We can use these inputs as the dual type to calculate the values for the hidden nodes. Using the image above as an example, _z_<sub>1</sub> is calculated using _x_<sub>1</sub> * _w_<sub>1</sub>, plus _x_<sub>2</sub> * _w_<sub>2</sub>. The ReLU function is applied to this result. The list of hidden nodes is returned from the `convnet()` function. We can use this list and the weights, _v_<sub>1</sub> to _v_<sub>4</sub>, to calculate the single output. This single output is also returned from the function in dual format.


I achieved 100% on this assignment.
