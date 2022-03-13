import Levenshtein
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import numpy as np
import fingerprint_generator as fg
def get_all_directory_distance(directories):
    result = dict.fromkeys(directories)
    d_c = dict.fromkeys(directories)
    for directory in directories:
        d_print = fg.directory_fingerprint(directory)
        print(directory)
        c_print = ''.join([s for s in fg.content_fingerprint(directory).splitlines(True) if s.strip()])
        d_c[directory] = [d_print,c_print]
    for directory_out in directories:
        tmp = []
        for directory_in in directories:
            dd = Levenshtein.distance(d_c[directory_out][0],d_c[directory_in][0])/max(len(d_c[directory_out][0]),len(d_c[directory_in][0]))
            tmp.append(dd)
        result[directory_out] = tmp
    return result
    for directory in directories:
        a = np.arange(64).reshape(result[directory])
        flat = a.flatten()
def get_all_content_distance(directories):
    result = dict.fromkeys(directories)
    d_c = dict.fromkeys(directories)
    for directory in directories:
        d_print = fg.directory_fingerprint(directory)
        c_print = ''.join([s for s in fg.content_fingerprint(directory).splitlines(True) if s.strip()])
        d_c[directory] = [d_print,c_print]
    for directory_out in directories:
        tmp = []
        for directory_in in directories:
            cd = 1-Levenshtein.distance(d_c[directory_out][1],d_c[directory_in][1])/max(len(d_c[directory_out][1]),len(d_c[directory_in][1]),1)
            tmp.append(cd)
        result[directory_out] = tmp
    return result
def draw(relate_data,directories):
    # all_data=[]
    # for i in range(100):
    #     all_data.append(relate_data)
    # all_data=np.vstack(all_data)

    tsne = TSNE(n_components=2)
    tsne.fit_transform(relate_data)
    two_emb = tsne.embedding_

    plt.scatter(two_emb[:, 0], two_emb[:, 1])
    for i in range(len(two_emb)):
        plt.annotate(str(i), xy = (two_emb[i][0], two_emb[i][1]),xytext=directories)  # 这里xy是需要标记的坐标，xytext是对应的标签坐标
    plt.title("mytitle")
    plt.savefig(f'./tmp.png')
    plt.close()

# plt.rcParams['figure.figsize'] = (20, 20)  ## 显示的大小
# fig = plot_embedding(t-sne_dataNumpy, labelNumpy, 't-sne test')
# ### plt.savefig() 一定在前，不然将会保存空白的图像
# plt.savefig('t-sne-test.jpg')
# plt.show(fig)

if __name__ == '__main__':
    ds = fg.get_dirctory()
    a1 = get_all_directory_distance(ds)
    a2 = get_all_content_distance(ds)
    data = np.array([item for item in a2.values()])
    draw(data,ds)
        # for i in range(len(ds)):
        #     if 0.01<= a2[d][i] < 0.8:
        #         print(d+" match "+ds[i] + ' similarity: '+str(a2[d][i]))
        #     if 0.01<=a1[d][i] < 0.8 :
        #         print(d + " match2 " + ds[i] + ' similarity: ' + str(a1[d][i]))
    # print()
    # print()