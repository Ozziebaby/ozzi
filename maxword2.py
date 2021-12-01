def biggest(alphabet):
    big=''
    for item in alphabet:
        if item > big:
            big = item
    return big
sentence= "hi juju"
print(biggest(sentence))