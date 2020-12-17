import subprocess

text = "куда вы удалились?"

cmd = "python3 /Users/dmitriosipov/my_research/deep_learning/text_generation/ru-gpts-for-telegram/generate_transformers.py"

cmd_args_model_type = "--model_type=gpt2"
cmd_args_model_path = "--model_name_or_path=sberbank-ai/rugpt3small_based_on_gpt2"
cmd_args_k = "--k=20"
cmd_args_p = "--p=0.9"
cmd_args_prompt = "--prompt='{}'".format(text)

p1 = subprocess.run("python3 /Users/dmitriosipov/my_research/deep_learning/text_generation/ru-gpts-for-telegram/generate_transformers.py --model_type=gpt2 --model_name_or_path=sberbank-ai/rugpt3small_based_on_gpt2 --k=20 --p=0.9 --prompt='{}'".format(text), shell=True, capture_output=True)


if __name__ == '__main__':
    print(p1.stdout.decode())
    #subprocess.run("python3 generate_transformers.py --model_type=gpt2 --model_name_or_path=sberbank-ai/rugpt3small_based_on_gpt2 --k=20 --p=0.9 --prompt='{}'".format( text), shell=True)
    #subprocess.run([cmd, cmd_args_model_type, cmd_args_model_path, cmd_args_k, cmd_args_p, cmd_args_prompt], shell=True)