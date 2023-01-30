
import matplotlib.pyplot as plt
from setuptools._vendor.packaging.tags import _mac_arch
import main as _main
import CF6



def crea_pelicula(peli):
    res = []
    for i in range(0,_main.N):
        z = CF6.func(peli[i])
        plt.plot(z[0],z[1],marker="o",color="red")
    plt.show()


if __name__ == "__main__":

    h = [[0.0001257371522492834, 1.5403715067753807],
[0.022128668153341163, 1.3442187831452874],
[0.039412876375766015, 1.254319819483695],
[0.060582058506773534, 1.1721049077995993],
[0.07570694346535138, 1.1480063134801586],
[0.08817028728594803, 1.1299901420763336],
[0.08817028728594803, 1.1299901420763336],
[0.08817028728594803, 1.1299901420763336],
[0.08817028728594803, 1.1299901420763336],
[0.18735331554508522, 1.0853795328529467],
[0.19876047861361684, 0.9962066914027045],
[0.21042833265504984, 0.9142927673413673],
[0.21811726489368977, 0.8461267587974165],
[0.2274985094264724, 0.7823310608997899],
[0.2373745251273952, 0.7307896529554561],
[0.24663517239136123, 0.6755841510751986],
[0.2604105747294361, 0.6545360174266965],
[0.2604105747294361, 0.6545360174266965],
[0.2604105747294361, 0.6545360174266965],
[0.2604105747294361, 0.6545360174266965],
[0.2604105747294361, 0.6545360174266965],
[0.2604105747294361, 0.6545360174266965],
[0.2604105747294361, 0.6545360174266965],
[0.41078012962801236, 0.6215174795998933],
[0.4146061220180445, 0.5739627640637063],
[0.4170872981703374, 0.5287052543318873],
[0.42171167671642673, 0.47810748823593924],
[0.4246279937078562, 0.44424312411663347],
[0.4283983414766156, 0.40235550407706966],
[0.4313900698564632, 0.37246181148428764],
[0.4355674242922112, 0.32334700542852135],
[0.4398469664938015, 0.3091208775985783],
[0.44441703457970994, 0.27430528642322566],
[0.45304827563431505, 0.2507058011112996],
[0.45304827563431505, 0.24512335979164654],
[0.45304827563431505, 0.24512335979164654],
[0.45304827563431505, 0.24512335979164654],
[0.45304827563431505, 0.24512335979164654],
[0.45304827563431505, 0.24512335979164654],
[0.45304827563431505, 0.24512335979164654],
[0.6237761687871911, 0.19512589232314695],
[0.6237761687871911, 0.1503736227348194],
[0.6237761687871911, 0.16212956648188812],
[0.6237761687871911, 0.1488309386907325],
[0.6304198074805047, 0.09574368342937235],
[0.6304198074805047, 0.09493897229856531],
[0.6304198074805047, 0.06524885632065919],
[0.6304198074805047, 0.055564304025524175],
[0.6304198074805047, 0.030181943189918167],
[0.6330290423281766, 0.014997040959417571],
[0.6374214474373867, -0.023321716810521188],
[0.6374214474373867, -0.03395458262354726],
[0.6374214474373867, -0.041769027224897955],
[0.638806391146227, -0.056325519725212686],
[0.638806391146227, -0.056325519725212686],
[0.638806391146227, -0.056325519725212686],
[0.638806391146227, -0.056325519725212686],
[0.638806391146227, -0.056325519725212686],
[0.8376278574518509, -0.21787797542420723],
[0.8376278574518509, -0.20822515175124276],
[0.8376278574518509, -0.19164739975089595],
[0.8376278574518509, -0.27548829764382127],
[0.8376278574518509, -0.25971288855823604],
[0.8376278574518509, -0.3476680270895804],
[0.8376278574518509, -0.30908267304156584],
[0.8376278574518509, -0.2402069593376344],
[0.8376278574518509, -0.3269749662309014],
[0.8376278574518509, -0.2402069593376344],
[0.8376278574518509, -0.33053568142705336],
[0.8376278574518509, -0.3150934713491115],
[0.8376278574518509, -0.35902854984622656],
[0.8376278574518509, -0.33502079149613145],
[0.8376278574518509, -0.30795172231386364],
[0.8376278574518509, -0.3476680270895804],
[0.8376278574518509, -0.36614267739476847],
[0.8376278574518509, -0.37740727861167156],
[0.8376278574518509, -0.3476680270895804],
[0.8376278574518509, -0.37740727861167156],
[0.8376278574518509, -0.37740727861167156],
[0.8376278574518509, -0.37740727861167156]]
    
    
