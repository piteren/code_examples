import rouge

# returns Rouge value/valueL
def rouge_12L(
        sen :str,
        ref :str,
        ev :rouge.Rouge=    None,
        R1=                 True,
        R2=                 True,
        RL=                 True):

    if not ev: ev = rouge.Rouge()
    metrics = [0,0,0]
    try:
        metrics = ev.get_scores(sen,ref)
        metrics = [
            metrics[0]['rouge-1']['f'],
            metrics[0]['rouge-2']['f'],
            metrics[0]['rouge-l']['f']]
    except ValueError: pass
    rm = []
    if R1: rm.append(metrics[0])
    if R2: rm.append(metrics[1])
    if RL: rm.append(metrics[2])
    if len(rm) == 1: rm = rm[0]
    return rm