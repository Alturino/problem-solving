from typing import List


def processLogs(logs: List[str], threshold: int):
    m = {}
    for log in logs:
        splittedLog = log.split(" ")

        sourceId = splittedLog[0]
        destinationId = splittedLog[1]

        if sourceId == destinationId:
            m[sourceId] = m.get(sourceId, 0) + 1
            continue
        m[sourceId] = m.get(sourceId, 0) + 1
        m[destinationId] = m.get(destinationId, 0) + 1

    res = []
    sortedM = sorted(m.items(), key=lambda x: x[1])
    print(m, sortedM)
    for k, v in sortedM:
        if v >= threshold:
            res.append(k)
    return res


print(processLogs(["88 99 200", "88 99 300", "99 32 100"], 2))
