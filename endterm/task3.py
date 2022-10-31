    from sklearn.neural_network import MLPClassifier
    from sklearn.metrics import accuracy_score
    import numpy as np
    import matplotlib.pyplot as plt
    def func(x):
        return 1/(1 + np.exp(-x))
    def sigmoid_deriv(x):
        return func(x)*(1-func(x))
    def forward(x,w1,w2,predict=False):
        a1 = np.matmul(x,w1)
        z1 = func(a1)
    #create and add bais
        bias = np.ones((len(z1),1))
        z1 = np.concatenate((bias,z1),axis=1)
        a2 = np.matmul(z1,w2)
        z2 = func(a2)
        if predict:
            return z2
            return a1,z1,a2,z2
    def backprop(a2,z0,z1,z2,y):
        delta2 = z2 - y
        Delta2 = np.matmul(z1.T,delta2)
        delta1 = (delta2.dot(w2[1:,:].T))*sigmoid_deriv(a1)
        Delta1 = np.matmul(z0.T,delta1)
        return delta2,Delta1,Delta2
    #dataset
    X = np.array([[1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]])
    #class
    y = np.array([[1],[1],[1],[0]])
    #weights
    w1 = 0
    w2 = 0
    #initialize learning rate
    lr = 0.1
    costs = [] #initiate epochs
    epochs = 10000
    m = len(X)
    #start training
    for i in range(epochs):
        a1,z1,a2,z2 = forward(X,w1,w2)
        delta2,Delta1,Delta2 = backprop(a2,X,z1,z2,y)
        w1 -= lr*(1/m)*Delta1
        w2 -= lr*(1/m)*Delta2
    # add costs to list for plotting
        c = np.mean(np.abs(delta2))
        costs.append(c)
        if i % 1000 == 0:
            print(f"iteration: {i}. Error: {c}")
    #training complete
            print("Training complete")
    #Make prediction
    z3 = forward(X,w1,w2,True)
    print("Precentages: ")
    print(z3)
    print("Predictions: ")
    print(np.round(z3))
    plt.plot(costs)
    plt.show()