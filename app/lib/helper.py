def listRealtionUser(table):
    data = table.query.all()
    tables = []
    for i in data:
        tables.append({
            "id": i.id,
            "name": i.nama
        })
    return tables


def listRelationFakultas(table):
    data = table.query.all()
    tables = []
    for i in data:
        tables.append({
            "id": i.id,
            "name": i.fakultas
        })

    return tables


def listRelationJurusan(table):
    data = table.query.all()
    tables = []
    for i in data:
        tables.append({
            "id": i.id,
            "name": i.jurusan
        })

    return tables


def listRelationSemester(table):
    data = table.query.all()
    tables = []
    for i in data:
        tables.append({
            "id": i.id,
            "name": i.semester
        })

    return tables
