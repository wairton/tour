from typing import Dict, List


def magic(a: Dict[str, int]) -> List[str]:
    return ["{}:{}".format(k, v) for k, v in a.items()]


magic({'a': 1})
