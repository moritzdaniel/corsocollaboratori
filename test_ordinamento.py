#Test part 

def test_num_array(number):
    if number<=0:
        print("errori sul numero di numeri da ordinare")
        return True
    return False

def test_reverse(array_num):
    decrease=array_num[0]
    for i in range (1,len(array_num)):
        if i<decrease:
            decrease=i
        else:
            print("i numeri non sono i ordine decrescente")
            return True
    return False