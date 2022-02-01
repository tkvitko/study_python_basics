def get_data_from_file(filename: str) -> list:
    """Функция парсинга логов"""

    result = []

    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()

            ip_address = line.split(' ')[0]
            props = line.split('"')[1]
            props_list = props.split(' ')
            http_method = props_list[0]
            request_path = props_list[1]

            result.append((ip_address, http_method, request_path))

    return result


if __name__ == '__main__':
    file_name = 'nginx_logs.txt'
    print(get_data_from_file(filename=file_name)[:10])
