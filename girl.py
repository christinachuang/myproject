from flask import Flask, render_template, request, jsonify
import collections
import sys
import json
import numpy as np
from svmutil import*
from svm import*
import random
import pickle

global tmp1
global tmp2
global tmp3
global tmp4
global cal
global total
global right
global click
global count
global sort_list
global number_list
global randomed
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("Female.htm",title = 'Home')



@app.route('/shirts_g/')
def shirts():
    global dictionary_list
    global number_list
    dictionary_list = { 1: {'title': '迪士尼系列印花短版T恤-04-女 $299','path': '../static/image/g/01.jpg','num': 'shirt1/','idx': '1'},
                        2: {'title': '迪士尼系列修身T-32-女 $199','path': '../static/image/g/02.jpg','num': 'shirt2/','idx': '2'},
	       	        3: {'title': '史努比落肩T-32-女 $249','path': '../static/image/g/03.jpg', 'num': 'shirt3/','idx': '3'},
                        4: {'title': '史努比印花Tee-37-女 $249','path': '../static/image/g/04.jpg', 'num': 'shirt4/','idx': '4'},
        	        5: {'title': 'Moomin印花T恤-F01-女 $249','path': '../static/image/g/05.jpg', 'num': 'shirt5/','idx': '5'},
		        6: {'title': 'Moomin印花T恤-02-女 $249','path': '../static/image/g/06.jpg', 'num': 'shirt6/','idx': '6'},
		        7: {'title': 'Lisa Larson印花T恤-F02-女 $249','path': '../static/image/g/07.jpg', 'num': 'shirt7/','idx': '7'},
	    	        8:{'title': 'Hallmark印花Tee-03-女 $290','path': '../static/image/g/08.jpg', 'num': 'shirt8/','idx': '8'},
			9: {'title': 'Hallmark Artist印花T恤-01-女 $290','path': '../static/image/g/09.jpg', 'num': 'shirt9/','idx': '9'},
			10: {'title': '竹節棉綁帶上衣-女 $299','path': '../static/image/g/10.jpg', 'num': 'shirt10/','idx': '10'},
    			11: {'title': '竹節棉印花短袖衫-女 $299','path': '../static/image/g/11.jpg', 'num': 'shirt11/','idx': '11'},
    			12: {'title': '短版圓領口袋短袖衫-女 $166','path': '../static/image/g/12.jpg', 'num': 'shirt12/','idx': '12'},
    			13: {'title': '竹節棉條紋短袖衫-女 $290','path': '../static/image/g/13.jpg', 'num': 'shirt13/','idx': '13'},
			14: {'title': 'Pima 棉羅紋V領T恤-女 $166','path': '../static/image/g/14.jpg', 'num': 'shirt14/','idx': '14'},
			15: {'title': '吸排配色背心-女 $166','path': '../static/image/g/15.jpg', 'num': 'shirt15/','idx': '15'},
			16: {'title': '吸排配色短袖衫-女 $299','path': '../static/image/g/16.jpg', 'num': 'shirt16/','idx':'16'},
			17: {'title': '吸排背心-女 $133','path': '../static/image/g/17.jpg', 'num': 'shirt17/','idx':'17'},
			18: {'title': '彈力細肩帶-女 $133','path': '../static/image/g/18.jpg', 'num': 'shirt18/','idx':'18'},
			19: {'title': '彈力短版交叉細肩帶-女 $149','path': '../static/image/g/19.jpg', 'num': 'shirt19/','idx':'19'},
			20: {'title': '嫘縈無袖襯衫-女 $490','path': '../static/image/g/20.jpg', 'num': 'shirt20/','idx':'20'},
			21: {'title': '柔軟格紋短袖上衣-女 $399','path': '../static/image/g/21.jpg', 'num': 'shirt21/','idx':'21'},
			22: {'title': '嫘縈綁帶洋裝-女 $590','path': '../static/image/g/22.jpg', 'num': 'shirt22/','idx':'22'},
			23: {'title': '兩件式雪紡印花洋裝-女 $399','path': '../static/image/g/23.jpg', 'num': 'shirt23/','idx':'23'},
			24: {'title': '純棉條紋七分袖長版衫-女 $490','path': '../static/image/g/24.jpg', 'num': 'shirt24/','idx':'24'},
			25: {'title': '純棉條紋七分袖長版衫-女 $490','path': '../static/image/g/25.jpg', 'num': 'shirt25/','idx':'25'},
			26: {'title': '文字印花毛圈連帽衫-女 $490','path': '../static/image/g/26.jpg', 'num': 'shirt26/','idx':'26'},
			27: {'title': '牛仔無袖洋裝-女 $590','path': '../static/image/g/27.jpg', 'num': 'shirt27/','idx':'27'},
			28: {'title': '配色圓領長袖T恤-女 $290','path': '../static/image/g/28.jpg', 'num': 'shirt28/','idx':'28'},
			29: {'title': '奇先生妙小姐七分袖T恤-02-女 $390','path': '../static/image/g/29.jpg', 'num': 'shirt29/','idx':'29'},
			30: {'title': '求爽爽印花T恤-女 $249','path': '../static/image/g/30.jpg', 'num': 'shirt30/','idx':'30'},
			31: {'title': 'Pepsi印花T恤-L01-女 $199','path': '../static/image/g/31.jpg', 'num': 'shirt31/','idx':'31'},
			32: {'title': 'Hallmark Artist印花T恤-01-女 $249','path': '../static/image/g/32.jpg', 'num': 'shirt32/','idx':'32'},
			33: {'title': '格紋綁帶短袖洋裝-女 $299','path': '../static/image/g/33.jpg', 'num': 'shirt33/','idx':'33'},
			34: {'title': '針織圓領背心-女 $399','path': '../static/image/g/34.jpg', 'num': 'shirt34/','idx':'34'},
			35: {'title': 'H.H先生 Wink-圓領反摺口袋T $249','path': '../static/image/g/35.jpg', 'num': 'shirt35/','idx':'35'},
			36: {'title': '馬來貘 Hide and seek-一字領條紋寬袖上衣 $299','path': '../static/image/g/36.jpg', 'num': 'shirt36/','idx':'36'},
			37: {'title': '爽爽貓 Look at you-圓領開岔長版T $350','path': '../static/image/g/37.jpg', 'num': 'shirt37/','idx':'37'},
			38: {'title': '馬來貘LOVE MORE英字母燙銀原創T恤 $249','path': '../static/image/g/38.jpg', 'num': 'shirt38/','idx':'38'},
			39: {'title': 'H.H先生 Kiss kiss-一字領寬袖上衣 $299','path': '../static/image/g/39.jpg', 'num': 'shirt39/','idx':'39'},
			40: {'title': '熱帶海邊 $199','path': '../static/image/g/40.jpg', 'num': 'shirt40/','idx':'40'},
			41: {'title': 'Attraction $199','path': '../static/image/g/41.jpg', 'num': 'shirt41/','idx':'41'},
			42: {'title': '大象 $199','path': '../static/image/g/42.jpg', 'num': 'shirt42/','idx':'42'},
			43: {'title': '燈泡 $199','path': '../static/image/g/43.jpg', 'num': 'shirt43/','idx':'43'},
			44: {'title': '來~笑一個 $199','path': '../static/image/g/44.jpg', 'num': 'shirt44/','idx':'44'},
			45: {'title': 'LUCK [幸運] $199','path': '../static/image/g/45.jpg', 'num': 'shirt45/','idx':'45'},
			46: {'title': '畫一隻兔(女) $199','path': '../static/image/g/46.jpg', 'num': 'shirt46/','idx':'46'},
			47: {'title': '強勁球風(女) $199','path': '../static/image/g/47.jpg', 'num': 'shirt47/','idx':'47'},
			48: {'title': '馬來貘LOVE MORE英字母燙銀原創T恤 $249','path': '../static/image/g/48.jpg', 'num': 'shirt48/','idx':'48'},
			49: {'title': 'Is love-極柔T $279','path': '../static/image/g/49.jpg', 'num': 'shirt49/','idx':'49'},
			50: {'title': 'Love $199','path': '../static/image/g/50.jpg', 'num': 'shirt50/','idx':'shirt50'},
                        51:{'title': 'Tsum Tsum系列Fleece連帽衫 $390', 'path': '../static/image/g/51.jpg', 'num': 'shirt51/', 'idx': '51'},
                        52:{'title': '竹節棉長版八分袖上衣 $390', 'path': '../static/image/g/52.jpg', 'num': 'shirt52/', 'idx': '52'},
                        53:{'title': '棉質束腰長版衫-女 $ 590', 'path': '../static/image/g/53.jpg', 'num': 'shirt53/', 'idx': '53'},
                        54:{'title': '粗針麻花圓領背心 $490', 'path': '../static/image/g/54.jpg', 'num': 'shirt54/', 'idx': '54'},
                        55:{'title': '迪士尼系列毛圈連帽衫 $690', 'path': '../static/image/g/55.jpg', 'num': 'shirt55/', 'idx': '55'},
                        56:{'title': '細針織中高領背心 $590', 'path': '../static/image/g/56.jpg', 'num': 'shirt56/', 'idx': '56'},
                        57:{'title': '迪士尼系列毛圈圓領衫 $590', 'path': '../static/image/g/57.jpg', 'num': 'shirt57/', 'idx': '57'},
                        58:{'title': '輕柔八分袖寬版T恤 $290', 'path': '../static/image/g/58.jpg', 'num': 'shirt58/', 'idx': '58'},
                        59:{'title': '棉質喀什米爾寬羅紋毛衣 $690', 'path': '../static/image/g/59.jpg', 'num': 'shirt59/', 'idx': '59'},
                        60:{'title': '輕柔剪接八分袖T恤 $390', 'path': '../static/image/g/60.jpg', 'num': 'shirt60/', 'idx': '60'},
                        61:{'title': '純棉條紋花式長袖上衣 $299', 'path': '../static/image/g/61.jpg', 'num': 'shirt61/', 'idx': '61'},
                        62:{'title': '刻字開衩帽T $290', 'path': '../static/image/g/62.jpg', 'num': 'shirt62/', 'idx': '62'},
                        63:{'title': '層次長袖T恤 $290', 'path': '../static/image/g/63.jpg', 'num': 'shirt63/', 'idx': '63'},
                        64:{'title': '奧樂氣球雞印花T恤 $199', 'path': '../static/image/g/64.jpg', 'num': 'shirt64/', 'idx': '64'},
                        65:{'title': '皮克斯系列印花T恤 $290', 'path': '../static/image/g/65.jpg', 'num': 'shirt65/', 'idx': '65'},
                        66:{'title': '雪紡條紋襯衫 $490', 'path': '../static/image/g/66.jpg', 'num': 'shirt66/', 'idx': '66'},
                        67:{'title': '圓領貼布刺繡兔子上衣 $790', 'path': '../static/image/g/67.jpg', 'num': 'shirt67/', 'idx': '67'},
                        68:{'title': '假兩件式長版雪紡拼接上衣 $860', 'path': '../static/image/g/68.jpg', 'num': 'shirt68/', 'idx': '68'},
                        69:{'title': '撞色V領印花開叉洋裝 $930', 'path': '../static/image/g/69.jpg', 'num': 'shirt69/', 'idx': '69'},
                        70:{'title': '寬鬆長版素面連帽休閒外套 $1150', 'path': '../static/image/g/70.jpg', 'num': 'shirt70/', 'idx': '70'},
                        71:{'title': '花環印花素面上衣 $889', 'path': '../static/image/g/71.jpg', 'num': 'shirt71/', 'idx': '71'},
                        72:{'title': '長版條紋拉鏈連帽外套 $960', 'path': '../static/image/g/72.jpg', 'num': 'shirt72/', 'idx': '72'},
                        73:{'title': '寬鬆長版條紋上衣 $890', 'path': '../static/image/g/73.jpg', 'num': 'shirt73/', 'idx': '73'},
                        74:{'title': 'V領露肩拼接刺繡雪紡上衣 $591', 'path': '../static/image/g/74.jpg', 'num': 'shirt74/', 'idx': '74'},
                        75:{'title': '假兩件式條紋拼接上衣 $950', 'path': '../static/image/g/75.jpg', 'num': 'shirt75/', 'idx': '75'},
                        76:{'title': '寬鬆印花拉鏈棉質上衣 $299', 'path': '../static/image/g/76.jpg', 'num': 'shirt76/', 'idx': '76'},
                        77:{'title': '條紋喇叭袖寬鬆棉質上衣 $630', 'path': '../static/image/g/77.jpg', 'num': 'shirt77/', 'idx': '77'},
                        78:{'title': '寬鬆蕾絲拼接條紋洋裝 $760', 'path': '../static/image/g/78.jpg', 'num': 'shirt78/', 'idx': '78'},
                        79:{'title': '前短後長七分袖條紋棉質上衣 $560', 'path': '../static/image/g/79.jpg', 'num': 'shirt79/', 'idx': '79'},
                        80:{'title': '七分袖圓領印花開叉洋裝 $790', 'path': '../static/image/g/80.jpg', 'num': 'shirt80/', 'idx': '80'},
                        81:{'title': '假兩件式字母刺繡破洞上衣 $960', 'path': '../static/image/g/81.jpg', 'num': 'shirt81/', 'idx': '81'},
                        82:{'title': '圓領素面鈕釦裝飾不規則上衣 $760', 'path': '../static/image/g/82.jpg', 'num': 'shirt82/', 'idx': '82'},
                        83:{'title': '翻領雨傘刺繡牛仔上衣 $672', 'path': '../static/image/g/83.jpg', 'num': 'shirt83/', 'idx': '83'},
                        84:{'title': '領口流蘇綁帶刺繡上衣 $690', 'path': '../static/image/g/84.jpg', 'num': 'shirt84/', 'idx': '84'},
                        85:{'title': '短袖印花打結雪紡上衣 $580', 'path': '../static/image/g/85.jpg', 'num': 'shirt85/', 'idx': '85'},
                        86:{'title': '短版V領綁帶連帽上衣 $850', 'path': '../static/image/g/86.jpg', 'num': 'shirt86/', 'idx': '86'},
                        87:{'title': '兩件式麂皮絨加荷葉袖針織上衣 $850', 'path': '../static/image/g/87.jpg', 'num': 'shirt87/', 'idx': '87'},
                        88:{'title': '假兩件式不規則荷葉邊上衣 $580', 'path': '../static/image/g/88.jpg', 'num': 'shirt88/', 'idx': '88'},
                        89:{'title': '翻領不規則素面無袖上衣 $730', 'path': '../static/image/g/89.jpg', 'num': 'shirt89/', 'idx': '89'},
                        90:{'title': '圓領袖口綁帶刺繡上衣 $614', 'path': '../static/image/g/90.jpg', 'num': 'shirt90/', 'idx': '90'},
                        91:{'title': '蕾絲拼接條紋無袖上衣 $550', 'path': '../static/image/g/91.jpg', 'num': 'shirt91/', 'idx': '91'},
                        92:{'title': '排釦袖落肩雪紡襯衫 $390', 'path': '../static/image/g/92.jpg', 'num': 'shirt92/', 'idx': '92'},
                        93:{'title': '胸交叉造型羅紋合身洋裝 $530', 'path': '../static/image/g/93.jpg', 'num': 'shirt93/', 'idx': '93'},
                        94:{'title': '細肩排釦口袋牛仔洋裝 $730', 'path': '../static/image/g/94.jpg', 'num': 'shirt94/', 'idx': '94'},
                        95:{'title': '流蘇綁帶圓領七分袖上衣 $590', 'path': '../static/image/g/95.jpg', 'num': 'shirt95/', 'idx': '95'},
                        96:{'title': '雙層荷葉領細肩帶縮腰洋裝 $695', 'path': '../static/image/g/96.jpg', 'num': 'shirt96/', 'idx': '96'},
                        97:{'title': '米奇款項鍊背心 $298', 'path': '../static/image/g/97.jpg', 'num': 'shirt97/', 'idx': '97'},
                        98:{'title': '透膚V領撞色條紋長袖針織上衣 $450', 'path': '../static/image/g/98.jpg', 'num': 'shirt98/', 'idx': '98'},
                        99:{'title': '挑戰極限T恤上衣 $390', 'path': '../static/image/g/99.jpg', 'num': 'shirt99/', 'idx': '99'},
                        100:{'title': 'lets surf T恤上衣 $90', 'path': '../static/image/g/100.jpg', 'num': 'shirt100/', 'idx': '100'},
                        101:{'title': '我的島嶼 T恤上衣 $390', 'path': '../static/image/g/101.jpg', 'num': 'shirt101/', 'idx': '101'},
                        102:{'title': '大V領配色坑紋針織上衣 $188', 'path': '../static/image/g/102.jpg', 'num': 'shirt102/', 'idx': '102'},
                        103:{'title': '坑條鈕扣合身薄織背心 $180', 'path': '../static/image/g/103.jpg', 'num': 'shirt103/', 'idx': '103'},
                        104:{'title': '削肩條紋背心 $219', 'path': '../static/image/g/104.jpg', 'num': 'shirt104/', 'idx': '104'},
                        105:{'title': '碎花細肩帶背心 $238', 'path': '../static/image/g/105.jpg', 'num': 'shirt105/', 'idx': '105'},
                        106:{'title': '坑條修身針織背心 $199', 'path': '../static/image/g/106.jpg', 'num': 'shirt106/', 'idx': '106'},
                        107:{'title': '側衩長版格紋襯衫 $336', 'path': '../static/image/g/107.jpg', 'num': 'shirt107/', 'idx': '107'},
                        108:{'title': '品牌字假兩件上衣 $417', 'path': '../static/image/g/108.jpg', 'num': 'shirt108/', 'idx': '108'},
                        109:{'title': '微高領七分袖上衣 $417', 'path': '../static/image/g/109.jpg', 'num': 'shirt109/', 'idx': '109'},
                        110:{'title': 'MIT 花紗剪裁大字上衣 $340', 'path': '../static/image/g/110.jpg', 'num': 'shirt110/', 'idx': '100'},
			} # fake user
					
    number_list = ['one','oneone','two','twotwo','three','threet','four','fourf','five','fivef','six','sixs','seven','sevens','eight','eighte','nine','ninen','ten','tent',
						'eleven','elevene','twelve','twelvet','thirteen','thirteent','fourteen','fourteenf','fifteen','fifteenf','sixteen','sixteens','seventeen','seventeens',
						'eighteen','eighteene','nineteen','nineteenn','twenty','twentyt','twenty1','twenty1t','twenty2','twenty2t','twenty3','twenty3t','twenty4','twenty4t',
						'twenty5','twenty5t','twenty6','twenty6t','twenty7','twenty7t','twenty8','twenty8t','twenty9','twenty9t','thirty','thirtyt','thirty1','thirty1t',
						'thirty2','thirty2t','thirty3','thirty3t','thirty4','thirty4t','thirty5','thirty5t','thirty6','thirty6t','thirty7','thirty7t','thirty8','thirty8t',
						'thirty9','thirty9t','fourty','fourtyf','fourty1','fourty1f','fourty2','fourty2f']

    global sort_list
    sort_list = collections.OrderedDict(dictionary_list)
    new_d = {}
    global randomed
    randomed={}
    randomed=random.sample(range(109),42)
    for idx in range(0, len(randomed)):
        randomed[idx]=randomed[idx]+1

    #randomed = {51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92}
    for key, value in sort_list.items():
        if key in randomed:
            new_d[key] = value
    print(new_d)
    return render_template("/shirts_g/shirts.htm",title = 'Home',list = new_d,classNum = number_list)

@app.route('/shirts_g/<shirt_id>/')
def rught_page_detail(shirt_id):
    if shirt_id == 'but.htm':
        param = []
        #Do SVM
        with open('../../libsvm-3.22/windows/save_all','r') as f:
            alist = [line.rstrip() for line in f]
            for idx in range(2, len(alist)):
                data = alist[idx].split()
                param.append(float(data[2]))
        cal_scal = np.zeros_like(cal)
        total_scal = np.zeros_like(total)
        right_scal = np.zeros_like(right)
        click_scal = np.zeros_like(click)

        for idx in range(0, len(cal)):
            cal_scal[idx] = -1+(1-(-1))*(cal[idx]-0)/(param[0]-0)
            total_scal[idx] = -1+(1-(-1))*(total[idx]-0)/(param[1]-0)
            right_scal[idx] = -1+(1-(-1))*(right[idx]-0)/(param[2]-0)
            click_scal[idx] = -1+(1-(-1))*(click[idx]-0)/(param[3]-0)
        model = svm_load_model("../../libsvm-3.22/python/testv3.model")
        new_la=[]
        new_ind=[]
        for idx in randomed:          
            x0, _ = gen_svm_nodearray({1:cal_scal[idx], 2:total_scal[idx], 3:right_scal[idx], 4:click_scal[idx]})
            label = libsvm.svm_predict(model, x0)
            new_la.append(label)
            new_ind.append(idx)
        print(new_la)
        new_d = {}
        recommand = []
        for idx in range(0, len(new_la)-1):
            if new_la[idx] == 5:
                recommand.append(new_ind[idx])
        print(recommand)
        #Recommandation System 
        number_of_image = 110
        sorted_sim = []
        #load file from disk
        with open ('matrixG', 'rb') as fp:
            sorted_sim = pickle.load(fp)
                
        #find the similar image
        rec_clothes = []
        chosen_images = []
        chosen_img = []
        chosen_images=recommand #6
        #chosen_images = [77]
        for k in range(len(chosen_images)):
            chosen_img = chosen_images[k]
            recommand_num = 3 #decide how many images to recommand
            for i in range(recommand_num):
                im_num = sorted_sim[chosen_img][i][1]
                rec_clothes.append(im_num+1)
        #print("cloth %d" %chosen_img)
        print(rec_clothes)

        for key, value in sort_list.items():
            if key in rec_clothes:
                new_d[key] = value
        sort_d = collections.OrderedDict(new_d)
        return render_template("/shirts_g/but.htm",title= 'Result', list = sort_d, classNum = number_list)
    else:
        return render_template("/shirts_g/%s/a.htm" %shirt_id)

@app.route('/pie',methods=['POST'])
def pie():
    global tmp1
    global tmp2
    global tmp3
    global tmp4
    global cal
    global total
    global right
    global click
    global count
    tmp1 = request.form.getlist('col_cal[]')
    tmp2 = request.form.getlist('col_total[]')
    tmp3 = request.form.getlist('col_right[]')
    tmp4 = request.form.getlist('col_click[]')
    tmp5 = request.form.getlist('col_count[]')
    cal = [float(i) for i in tmp1]
    total = [float(i) for i in tmp2]
    right = [float(i) for i in tmp3]
    click = [float(i) for i in tmp4]
    count = [float(i) for i in tmp5]
    #print(click)


if __name__ == "__main__":
	app.debug=True
	app.run()
