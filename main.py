import asyncio


async def get_matrix(url):
    import requests

    async def url_to_matrix(url):
        loop = asyncio.get_event_loop()
        res = await loop.run_in_executor(None, requests.get, url)
        if res.status_code in range(400, 601):
            print("Error: ", res.status_code)
            return []

        matrix = []
        temp = []
        n = (len(res.text.split("\n")) - 2) // 2
        m = 0
        for elem in res.text.split():
            if elem.isdigit():
                temp.append(int(elem))
                m += 1
            if m == n:
                matrix.append(temp)
                temp = []
                m = 0
        return matrix


    async def read_matrix(matrix):
        res = []
        n = len(matrix)
        m = 0
        for v in range(n // 2):
            # Заполнение верхней горизонтальной матрицы
            for i in range(n - m):
                res.append(matrix[i + v][v])

            # Заполнение левой вертикальной матрицы
            for i in range(v + 1, n - v):
                res.append(matrix[-v - 1][i])

            # Заполнение нижней горизонтальной матрицы
            for i in range(v + 1, n - v):
                res.append(matrix[-i - 1][-v - 1])

            # Заполнение правой вертикальной матрицы
            for i in range(v + 1, n - (v + 1)):
                res.append(matrix[v][-i - 1])
            m += 2
        return res

    matrix = await url_to_matrix(url)
    read = await read_matrix(matrix)
    return read

# SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
# TRAVERSAL = [
#     10, 50, 90, 130,
#     140, 150, 160, 120,
#     80, 40, 30, 20,
#     60, 100, 110, 70,
# ]


# def test_get_matrix():
#     assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSAL


# test_get_matrix()
