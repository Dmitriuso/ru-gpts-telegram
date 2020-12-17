import argparse

def text_gen(args):
    input_text = args.enter_text if args.enter_text else "doesn't work"
    return print(input_text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--enter_text", default=None, type=str, required=True)
    output = text_gen(args)
    return output


