# Training and evaluation loop

from multi_class import *

# Create a loss function
loss_fn = nn.CrossEntropyLoss()

# Create an optimizer
optimizer = torch.optim.SGD(params=model_4.parameters(), lr=0.1)

# Create an accuracy function
def accuracy_fn(y_true, y_pred):
    correct = torch.eq(y_true, y_pred).sum().item()
    acc = (correct/len(y_pred)) * 100
    return acc

model_4.eval()
with torch.inference_mode():
    y_logits = model_4(x_test)

y_inf_prob = torch.softmax(y_logits, dim=1)
y_inf_label = torch.argmax(y_inf_prob, dim=1)

# Create a training loop
torch.manual_seed(42)
epochs = 100

print(y_inf_prob)
print(y_inf_label)

for epoch in range(epochs):
    model_4.train()

    y_logits = model_4(x_train)
    y_pred = torch.softmax(y_logits, dim=1).argmax(dim=1)

    loss = loss_fn(y_logits, y_train)
    acc = accuracy_fn(y_true=y_train, y_pred=y_pred)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    model_4.eval()
    with torch.inference_mode():
        test_logits = model_4(x_test)
        test_inf = torch.softmax(test_logits, dim=1).argmax(dim=1)

        test_loss = loss_fn(test_logits, y_test)
        test_acc = accuracy_fn(y_true=y_test, y_pred=test_inf)

    if epoch % 10 == 0:
        print(f"Epoch: {epoch} | Loss: {loss: .4f}, | Acc: {acc: .2f}, | Test loss: {test_loss: .4f}, | Test acc: {test_acc: .2f}")

