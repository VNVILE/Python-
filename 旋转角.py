while True:
    xuan_ze_0 = input("你知道的条件是？  【1】将对应点连接旋转中心后，整个图形被分成的块数  【2】最小旋转角或最大旋转角")
    if xuan_ze_0 == "1":


        kuai_shu = input("将对应点连接旋转中心后，整个图形被分成的块数。:")
        small = 360 / int(kuai_shu)

        print("这是最小旋转角:")
        print(int(small))

        print("下列是所有旋转角    ")

        print(small * 2)
        print(small * 3)
        print(small * 4)
        print(small * 5)
        print(small * 6)
        print(small * 7)
        print(small * 8)
        print(small * 9)

        print('最大旋转角为：')
        big = 360 - int(small)
        print(big)


        xuan_ze_1 = input("继续请输1，重来请输2")


        if xuan_ze_1 == 1:
            print("继续")

        else:
            if xuan_ze_1 == 2:
                print("重来")

                while True:
                    kuai_shu = input("将对应点连接旋转中心后，整个图形被分成的块数。:")
                    small = 360 / int(kuai_shu)

                    print("这是最小旋转角:")
                    print(int(small))

                    print("下列是所有旋转角    ")

                    print(small * 2)
                    print(small * 3)
                    print(small * 4)
                    print(small * 5)
                    print(small * 6)
                    print(small * 7)
                    print(small * 8)
                    print(small * 9)


                    print('最大旋转角为：')
                    big = 360 - int(s)
                    print(big)

                    xuan_ze_2 = input("继续请输1，重来请输2")
                    if xuan_ze_2 == 1:
                        print("继续：")
                        break
                    else:
                        if xuan_ze_2 == 2:
                            print("重来：")


    else:
        while True:

            xuan_ze_3 = input("反求：将对应点连接旋转中心后，整个图形被分成的块数，请问您知道的条件是：\n" + "[1]最小旋转角  [2]最大旋转角")

            if xuan_ze_3 == "1":
                x = input("反求：将对应点连接旋转中心后，整个图形被分成的块数，最小旋转角为:")
                c = 360 / int(x)
                print(int(c))

            else:
                if xuan_ze_3 == "2":
                    x = input("反求：将对应点连接旋转中心后，整个图形被分成的块数，最大旋转角为:")
                    c = 360 / (360 - int(x))
                    print(c)
            xuan_ze_4 = input("继续请输1，重来请输2")

            if xuan_ze_4 == 1:
                print("继续")
                break

            else:

                if xuan_ze_4 == 2:
                    print("重来")



























