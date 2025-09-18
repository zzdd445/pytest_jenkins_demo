import yaml

# file_path = "../data/data.yaml"
def read_yaml(file_path):
    # 读取yaml文件
    with open(file_path,"r",encoding="utf-8") as f:
        data = yaml.safe_load(f)
        list_data = []
        for key,value in data['test_data'].items():
            list_data.append((key,value['num1'], value['num2'], value['sum']))
    return list_data

if __name__ == '__main__':
    list_data = read_yaml(file_path)
    print(list_data)
