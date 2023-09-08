import modpie
z = 12
def outer():
    print (f'y in outer before assig:{"y" in locals()}')
    y = 12
    print (f'y in outer after assig:{"y" in locals()}')
    def answer():
        asdas = 12 + y + z 
        print (f'y in answer:{"y" in locals()}')
        print(locals())
        print(globals())
        return x
    return answer()

if __name__ == '__main__':
    x = 42
    print(f'x' in main exists: {"y" in locals()}) # locals - все переменные которые существуют сейчас, globals - вообще все переменные
    #outer()
    print(y)
 