import json

def load_candidates():
    '''
    Загружает даныне из файла
    '''
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all():
    '''
    Показывает всех кандидатов
    '''
    return load_candidates()


def get_by_pk(pk):
    '''
    Возращает кандидатов по pk
    '''
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate
    return


def get_by_skill(skill):
    '''
    Возвращает кандиадтов по навыку
    '''
    candidates = []
    for candidate in load_candidates():
        if skill.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates

