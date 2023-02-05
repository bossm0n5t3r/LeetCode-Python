import os
from re import sub


class InitLeetCode:
    def __init__(self):
        problem_name = input("INPUT LEETCODE PROBLEM NAME: ")
        problem_name = problem_name.replace("II", "2")
        problem_url = input("INPUT LEETCODE PROBLEM URL: ")

        print("ENTER/PASTE YOUR PROBLEM SAMPLE. ONE MORE ENTER TO SAVE IT.")
        problem_sample = []
        while True:
            try:
                line = input()
                if len(line) == 0:
                    break
            except EOFError:
                break
            problem_sample.append(line)

        print("ENTER/PASTE YOUR PROBLEM EXAMPLES. ONE MORE ENTER TO SAVE IT.")
        problem_examples = []
        while True:
            try:
                line = input()
                if len(line) == 0:
                    break
            except EOFError:
                break
            problem_examples.append(line)

        problem_params = input("INPUT LEETCODE PROBLEM PARAMS: ")

        first_dot_index = problem_name.index(".")
        problem_name_except_number = problem_name[first_dot_index + 1:].strip()

        self.problem = {
            "name": problem_name,
            "name_except_number": problem_name_except_number,
            "url": problem_url,
            "sample": problem_sample,
            "params": problem_params,
            "examples": problem_examples,
        }

    @staticmethod
    def __camel_case(s):
        s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
        return ''.join([s[0].lower(), s[1:]])

    @staticmethod
    def __pascal_case(s):
        s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
        return ''.join(s)

    def create_folder(self):
        directory = "./" + self.__camel_case(self.problem["name_except_number"])
        self.problem["directory"] = directory
        if not os.path.exists(directory):
            os.makedirs(directory)

    def create_readme(self):
        directory = self.problem["directory"]
        filename = "README.md"
        file_path = os.path.join(directory, filename)
        if not os.path.exists(file_path):
            with open(file_path, 'wb') as read_me:
                read_me.write(("# " + self.problem["name"] + "\n").encode('utf-8'))
                read_me.write("\n".encode('utf-8'))
                read_me.write(("- [" + self.problem["url"] + "](" + self.problem["url"] + ")\n").encode('utf-8'))
                read_me.write("".encode('utf-8'))
        else:
            print(filename + " ALREADY EXISTS")

    def create_problem(self):
        directory = self.problem["directory"]
        filename = self.__pascal_case(self.problem["name_except_number"]) + ".py"
        file_path = os.path.join(directory, filename)
        if not os.path.exists(file_path):
            with open(file_path, 'wb') as problem_file:
                sample = self.problem["sample"]
                for line in sample:
                    line = line.replace("List", "list")
                    problem_file.write((line + "\n").encode('utf-8'))

                problem_file.write("\n".encode('utf-8'))
                problem_file.write("    def test(self):\n".encode('utf-8'))
                problem_file.write("        tests = [\n".encode('utf-8'))
                example_spaces = "            ["

                examples = self.problem["examples"]
                for line in examples:
                    problem_file.write((example_spaces + line + "],\n").encode('utf-8'))

                problem_file.write("        ]\n".encode('utf-8'))
                problem_file.write("        for test in tests:\n".encode('utf-8'))
                problem_file.write(
                    ("            " + self.problem["params"] + ",expect_result = test\n").encode('utf-8')
                )
                problem_file.write("            result = self\n".encode('utf-8'))
                problem_file.write("            print(result)\n".encode('utf-8'))
                problem_file.write("            print(result == expect_result)\n".encode('utf-8'))
                problem_file.write("\n".encode('utf-8'))
                problem_file.write("\n".encode('utf-8'))
                problem_file.write("if __name__ == '__main__':\n".encode('utf-8'))
                problem_file.write("    Solution().test()\n".encode('utf-8'))
        else:
            print(filename + " ALREADY EXISTS")

    def init(self):
        self.create_folder()
        self.create_readme()
        self.create_problem()


if __name__ == '__main__':
    InitLeetCode().init()
