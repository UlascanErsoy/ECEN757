import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("id", type=int)
    parser.add_argument("-m", type=int)
    parser.add_argument("-s", type=int)
    parser.add_argument("--skip", type=int)

    args = parser.parse_args()

    nodes = [idx for idx in range(args.s, 2**args.m, args.skip)]

    print(f"{len(nodes)} Nodes!")

    print("\ti\t|\tft[i]")
    print("-"*35)
    for idx in range(args.m):
        mm = (args.id + 2**idx)%(2**args.m)
        val= [i for i in nodes if i >= mm][0]
        print(f"\t{idx}\t|\t{val}")
