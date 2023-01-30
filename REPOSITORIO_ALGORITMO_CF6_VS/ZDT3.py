# Test problem definitions */
import main as _main
import numpy as np
import math 

PI = 3.14159265358979

'''  Test problem ZDT3
    # of real variables = 30
    # of bin variables = 0
    # of objectives = 2
    # of constraints = 0
'''

def func(xreal):
    obj = [0.0,0.0]
    obj[0] = xreal[0]
    for i in range(2,_main.D1):
        tmp += xreal[i]
    g=1+((9*tmp)/(_main.N-1))
    h=1-math.sqrt(xreal[0]/g)-(xreal[0]/g)*math.sin(10*PI*xreal[0]);
    obj[1] = g*h;
    return [obj[0],obj[1]];


'''
if __name__ == "__main__":
    a = [0.7089051190741016, 0.6839051190741016, 0.6330857957167183, 0.9713529302501285, 0.7062289945591429, 0.017174572362197008, 0.11854582763973834, 0.823657678632213, 0.025055874697786473, 0.21854582763973834, 0.11854582763973834, 0.14354582763973833, 0.09354582763973833, 0.16854582763973835, 0.9996686629115362, 0.11854582763973834, 0.4498436273189912, 0.4065388923169982, 0.5303293586695488, 0.7285966754357848, 0.5089197075787103, 0.4589197075787103, 0.37183020456160965, 0.6041514628312292, 0.3069541663641312, 0.29051008327841943, 0.4655070040620591, 0.6702816083368164, 0.605452451963462, 0.6702816083368164, 0.47748608257427383, 0.3655070040620591]
    b = [0.8718278936781675, 0.8968278936781675, 0.5198151842450398, 0.9916315799536177, 0.9444210533024118, 0.7580206839146342, 0.7580206839146342, 0.7080206839146341, 0.2814886543752405, 0.3122063170214117, 0.4767373615908971, 0.3563401927684681, 0.2314886543752405, 0.07432227971049948, 0.16357368569056377, 0.005670024019420072, 0.29714674281289544, 0.5426700520019349, 0.48131094000886987, 0.4313109400088698, 0.8072720253738002, 0.49931822420186883, 0.5610852652662546, 0.4632252931556551, 0.6960607909153307, 0.6343249611056355, 0.7639974032168309, 0.5417159472536824, 0.5253963606585856, 0.6434720888704158, 0.5017639773398915, 0.4337848554787772]
    c = [0.8291632737964687, 0.7304362388373207, 0.9063121667270153, 1.0, 0.5771780918254221, 0.6498294644530823, 0.7024484153497539, 0.3680359540529702, 0.9651692626487576, 0.33060165988517654, 0.8483159354307034, 0.7032031912013517, 0.040836233833769886, 0.3036309594740485, 0.3304469923928947, 0.7650656152381925, 0.43969691105227193, 0.3450485444011067, 0.8295352642525611, 0.4700078734705646, 0.4200078734705646, 0.6261657721708864, 0.16107467437134243, 0.4200078734705646, 0.5113140687909172, 0.5529267424862367, 0.7346792699940108, 0.5561015063924946, 0.6739574989506154, 0.8137459305646526,1.674722e-01]
    d =  [7.372373e-01  ,  2.408622e-01    ,6.150541e-01 ,   3.884384e-01 ,   6.873944e-02 ,   1.330111e-01   , 5.641124e-01  ,  1.131620e-01 ,   6.324599e-02,    2.655100e-02   , 3.135216e-01,    8.650114e-01,    1.938405e-01    ,4.774394e-01    ,1.636881e-01    ,9.907459e-02,    3.204181e-01  ,  6.655801e-01   , 5.182136e-01 ,   7.930005e-01  ,  4.850696e-01 ,   4.136453e-01   , 9.986325e-01  ,  8.145963e-02 ,   6.962571e-01,    6.447676e-01   , 4.623648e-01,    7.247345e-02,    9.599600e-01,1.674722e-01]
    #bb = np.array([0.3,0.7])
    #print(d.__len__())
    res = func(d)
    print(res)
'''