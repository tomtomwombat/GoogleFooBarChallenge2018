from fractions import Fraction

def floor_sum(n, ratio):
    if n <= 0: return 0
    arth_sum = lambda x: int(x * (x + 1) / 2)
    
    frac = ratio - int(ratio)
    base = arth_sum(n) * int(ratio)

    height = int(n*frac)
    base += n*height

    new_ratio = 1/frac
    new_frac = new_ratio - int(new_ratio)
    
    base -= arth_sum(height) * int(new_ratio)
    base -= floor_sum(height, new_frac)
    return base
    

def solution(n):
    rt = "141421356237309504880168872420969807856967187537694807317667973"+\
          "79907324784621070388503875343276415727350138462309122970249248"+\
          "36055850737212644121497099935831413222665927505592755799950501"+\
          "15278206057147010955997160597027453459686201472851741864088919"+\
          "86095523292304843087143214508397626036279952514079896872533965"+\
          "46331808829640620615258352395054745750287759961729835575220337"+\
          "53185701135437460340849884716038689997069900481503054402779031"+\
          "64542478230684929369186215805784631115966687130130156185689872"+\
          "37235288509264861249497715421833420428568606014682472077143585"+\
          "48741556570696776537202264854470158588016207584749226572260020"+\
          "8558446652145839"

    ratio = Fraction(int(rt), 10**(len(rt)-1))
    return str(floor_sum(int(n), ratio))



print(solution(77))