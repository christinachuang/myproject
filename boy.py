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
    return render_template("Male.htm",title = 'Home')



@app.route('/shirts_b/')
def shirts():
    global dictionary_list
    global number_list
    dictionary_list = { 1: {'title': '米奇款BOX連帽T $672','path': '../static/image/b/01.jpg','num': 'shirt1/','idx': '1'},
                        2: {'title': 'MIT 品牌文字短T $417','path': '../static/image/b/02.jpg','num': 'shirt2/','idx': '2'},
	       	        3: {'title': 'MIT 布魯托款厚短T $417','path': '../static/image/b/03.jpg', 'num': 'shirt3/','idx': '3'},
                        4: {'title': '衝浪極限 $199','path': '../static/image/b/04.jpg', 'num': 'shirt4/','idx': '4'},
        	        5: {'title': 'Action $199','path': '../static/image/b/05.jpg', 'num': 'shirt5/','idx': '5'},
		        6: {'title': 'Banana $199','path': '../static/image/b/06.jpg', 'num': 'shirt6/','idx': '6'},
		        7: {'title': 'free $199','path': '../static/image/b/07.jpg', 'num': 'shirt7/','idx': '7'},
	    	        8:{'title': '客製化 $199','path': '../static/image/b/08.jpg', 'num': 'shirt8/','idx': '8'},
			9: {'title': '經典水洗原色圓領素T-黑 $199','path': '../static/image/b/09.jpg', 'num': 'shirt9/','idx': '9'},
			10: {'title': '經典水洗原色圓領素T-白 $199','path': '../static/image/b/10.jpg', 'num': 'shirt10/','idx': '10'},
    			11: {'title': '經典水洗原色圓領素T-丈青 $199','path': '../static/image/b/11.jpg', 'num': 'shirt11/','idx': '11'},
    			12: {'title': '經典水洗原色圓領素T-麻灰 $199','path': '../static/image/b/12.jpg', 'num': 'shirt12/','idx': '12'},
    			13: {'title': '經典水洗原色圓領素T-麻花藍 $199','path': '../static/image/b/13.jpg', 'num': 'shirt13/','idx': '13'},
			14: {'title': '條紋針織毛衣-藍 $607','path': '../static/image/b/14.jpg', 'num': 'shirt14/','idx': '14'},
			15: {'title': '立體結紗針織毛衣-丈青 $607','path': '../static/image/b/15.jpg', 'num': 'shirt15/','idx': '15'},
			16: {'title': 'V領素色細針針織毛衣-麻灰藍 $431','path': '../static/image/b/16.jpg', 'num': 'shirt16/','idx':'16'},
			17: {'title': '掰掰啾啾 What?-圓領短袖T-麻灰 $199','path': '../static/image/b/17.jpg', 'num': 'shirt17/','idx':'17'},
			18: {'title': '馬來貘 Camping-圓領短袖T-黑 $133','path': '../static/image/b/18.jpg', 'num': 'shirt18/','idx':'18'},
			19: {'title': '簡約正裝長袖襯衫-藍白細格 $607','path': '../static/image/b/19.jpg', 'num': 'shirt19/','idx':'19'},
			20: {'title': '簡約正裝長袖襯衫-深藍 $607','path': '../static/image/b/20.jpg', 'num': 'shirt20/','idx':'20'},
			21: {'title': '簡約正裝長袖襯衫-藍白格 $607','path': '../static/image/b/21.jpg', 'num': 'shirt21/','idx':'21'},
			22: {'title': '沈默的隱身-刷毛連帽T $590','path': '../static/image/b/22.jpg', 'num': 'shirt22/','idx':'22'},
			23: {'title': '東京夜景 $399','path': '../static/image/b/23.jpg', 'num': 'shirt23/','idx':'23'},
			24: {'title': 'Choppers $190','path': '../static/image/b/24.jpg', 'num': 'shirt24/','idx':'24'},
			25: {'title': 'NOLimit $190','path': '../static/image/b/25.jpg', 'num': 'shirt25/','idx':'25'},
			26: {'title': '相信 $190','path': '../static/image/b/26.jpg', 'num': 'shirt26/','idx':'26'},
			27: {'title': 'homework $290','path': '../static/image/b/27.jpg', 'num': 'shirt27/','idx':'27'},
			28: {'title': 'barber $290','path': '../static/image/b/28.jpg', 'num': 'shirt28/','idx':'28'},
			29: {'title': '月圓派對 $390','path': '../static/image/b/29.jpg', 'num': 'shirt29/','idx':'29'},
			30: {'title': '獅子大開口 $249','path': '../static/image/b/30.jpg', 'num': 'shirt30/','idx':'30'},
			31: {'title': 'Believeit $199','path': '../static/image/b/31.jpg', 'num': 'shirt31/','idx':'31'},
			32: {'title': '毫無疑問 $249','path': '../static/image/b/32.jpg', 'num': 'shirt32/','idx':'32'},
			33: {'title': '燈泡 $299','path': '../static/image/b/33.jpg', 'num': 'shirt33/','idx':'33'},
			34: {'title': '衝浪極限 $399','path': '../static/image/b/34.jpg', 'num': 'shirt34/','idx':'34'},
			35: {'title': 'LUCK [幸運] $199','path': '../static/image/b/35.jpg', 'num': 'shirt35/','idx':'35'},
			36: {'title': 'XY基因染色體 $299','path': '../static/image/b/36.jpg', 'num': 'shirt36/','idx':'36'},
			37: {'title': 'V領竹節棉口袋素T-麻灰 $350','path': '../static/image/b/37.jpg', 'num': 'shirt37/','idx':'37'},
			38: {'title': '圓領竹節棉口袋素T-復古紅 $249','path': '../static/image/b/38.jpg', 'num': 'shirt38/','idx':'38'},
			39: {'title': '極柔原色V領素T-丈青 $299','path': '../static/image/b/39.jpg', 'num': 'shirt39/','idx':'39'},
			40: {'title': 'MIT 旗型文字短T $417','path': '../static/image/b/40.jpg', 'num': 'shirt40/','idx':'40'},
			41: {'title': '極柔原色V領素T-軍綠 $199','path': '../static/image/b/41.jpg', 'num': 'shirt41/','idx':'41'},
			42: {'title': '極柔原色V領素T-玫瑰紅 $199','path': '../static/image/b/42.jpg', 'num': 'shirt42/','idx':'42'},
			43: {'title': '手繪蘋果短T $299','path': '../static/image/b/43.jpg', 'num': 'shirt43/','idx':'43'},
			44: {'title': '沒時間愛人大學長T $599','path': '../static/image/b/44.jpg', 'num': 'shirt44/','idx':'44'},
			45: {'title': '口是心非大學長T $599','path': '../static/image/b/45.jpg', 'num': 'shirt45/','idx':'45'},
			46: {'title': '彩色人生大學長T $599','path': '../static/image/b/46.jpg', 'num': 'shirt46/','idx':'46'},
			47: {'title': '準備出發短T $199','path': '../static/image/b/47.jpg', 'num': 'shirt47/','idx':'47'},
			48: {'title': '猜名字短T $249','path': '../static/image/b/48.jpg', 'num': 'shirt48/','idx':'48'},
			49: {'title': '僨世標語短T $279','path': '../static/image/b/49.jpg', 'num': 'shirt49/','idx':'49'},
			50: {'title': '超人吸排運動短T $499','path': '../static/image/b/50.jpg', 'num': 'shirt50/','idx':'shirt50'},
            51:{'title': '蝙蝠俠吸排運動短T $390', 'path': '../static/image/b/51.jpg', 'num': 'shirt51/', 'idx': '51'},
            52:{'title': '不要濫用藥物短T $390', 'path': '../static/image/b/52.jpg', 'num': 'shirt52/', 'idx': '52'},
            53:{'title': '熱感應漫畫米奇款短T $ 590', 'path': '../static/image/b/53.jpg', 'num': 'shirt53/', 'idx': '53'},
            54:{'title': '線框BOX短T $490', 'path': '../static/image/b/54.jpg', 'num': 'shirt54/', 'idx': '54'},
            55:{'title': '配色粗條紋針織毛衣 $690', 'path': '../static/image/b/55.jpg', 'num': 'shirt55/', 'idx': '55'},
            56:{'title': '飄落的羽葉 $590', 'path': '../static/image/b/56.jpg', 'num': 'shirt56/', 'idx': '56'},
            57:{'title': 'MOONCITY $400', 'path': '../static/image/b/57.jpg', 'num': 'shirt57/', 'idx': '57'},
            58:{'title': '三角貓咪短T $290', 'path': '../static/image/b/58.jpg', 'num': 'shirt58/', 'idx': '58'},
            59:{'title': '別再傷心短T $290', 'path': '../static/image/b/59.jpg', 'num': 'shirt59/', 'idx': '59'},
            60:{'title': 'Sky Day-刷毛連帽T $390', 'path': '../static/image/b/60.jpg', 'num': 'shirt60/', 'idx': '60'},
            61:{'title': '天狼星的咆哮-刷毛連帽T $699', 'path': '../static/image/b/61.jpg', 'num': 'shirt61/', 'idx': '61'},
            62:{'title': '眼鏡衝浪短T $290', 'path': '../static/image/b/62.jpg', 'num': 'shirt62/', 'idx': '62'},
            63:{'title': '美味起司短T $290', 'path': '../static/image/b/63.jpg', 'num': 'shirt63/', 'idx': '63'},
            64:{'title': '好麻吉短T $199', 'path': '../static/image/b/64.jpg', 'num': 'shirt64/', 'idx': '64'},
            65:{'title': '西岸海灘BOX短T $290', 'path': '../static/image/b/65.jpg', 'num': 'shirt65/', 'idx': '65'},
            66:{'title': 'DOUBLE BOX短T $490', 'path': '../static/image/b/66.jpg', 'num': 'shirt66/', 'idx': '66'},
            67:{'title': '紐約城BOX短T $790', 'path': '../static/image/b/67.jpg', 'num': 'shirt67/', 'idx': '67'},
            68:{'title': '超人logo鋼印短T $860', 'path': '../static/image/b/68.jpg', 'num': 'shirt68/', 'idx': '68'},
            69:{'title': '蝙蝠俠爆裂吸排短T $930', 'path': '../static/image/b/69.jpg', 'num': 'shirt69/', 'idx': '69'},
            70:{'title': '緞帶文字短T $1150', 'path': '../static/image/b/70.jpg', 'num': 'shirt70/', 'idx': '70'},
            71:{'title': '反光BOX短T $889', 'path': '../static/image/b/71.jpg', 'num': 'shirt71/', 'idx': '71'},
            72:{'title': '龜裂紋球衣背心 $960', 'path': '../static/image/b/72.jpg', 'num': 'shirt72/', 'idx': '72'},
            73:{'title': '胸口條球衣背心 $890', 'path': '../static/image/b/73.jpg', 'num': 'shirt73/', 'idx': '73'},
            74:{'title': '薄類牛仔襯衫 $591', 'path': '../static/image/b/74.jpg', 'num': 'shirt74/', 'idx': '74'},
            75:{'title': '花紗口袋短T $950', 'path': '../static/image/b/75.jpg', 'num': 'shirt75/', 'idx': '75'},
            76:{'title': '小彩虹短T $299', 'path': '../static/image/b/76.jpg', 'num': 'shirt76/', 'idx': '76'},
            77:{'title': '魔術方塊短T $630', 'path': '../static/image/b/77.jpg', 'num': 'shirt77/', 'idx': '77'},
            78:{'title': '馬賽克短T $760', 'path': '../static/image/b/78.jpg', 'num': 'shirt78/', 'idx': '78'},
            79:{'title': 'V領眼鏡米奇款短T $560', 'path': '../static/image/b/79.jpg', 'num': 'shirt79/', 'idx': '79'},
            80:{'title': '大理石相片短T $790', 'path': '../static/image/b/80.jpg', 'num': 'shirt80/', 'idx': '80'},
            81:{'title': '圓章POLO衫 $460', 'path': '../static/image/b/81.jpg', 'num': 'shirt81/', 'idx': '81'},
            82:{'title': '電繡LOGO字短T $760', 'path': '../static/image/b/82.jpg', 'num': 'shirt82/', 'idx': '82'},
            83:{'title': '吸排運動背心 $672', 'path': '../static/image/b/83.jpg', 'num': 'shirt83/', 'idx': '83'},
            84:{'title': '反光口袋短T $690', 'path': '../static/image/b/84.jpg', 'num': 'shirt84/', 'idx': '84'},
            85:{'title': '條紋長版短T-白 $580', 'path': '../static/image/b/85.jpg', 'num': 'shirt85/', 'idx': '85'},
            86:{'title': '條紋長版短T-黑 $850', 'path': '../static/image/b/86.jpg', 'num': 'shirt86/', 'idx': '86'},
            87:{'title': '異色領條文短T $850', 'path': '../static/image/b/87.jpg', 'num': 'shirt87/', 'idx': '87'},
            88:{'title': '寬距細條紋短T $580', 'path': '../static/image/b/88.jpg', 'num': 'shirt88/', 'idx': '88'},
            89:{'title': '破版條軟棉短T $730', 'path': '../static/image/b/89.jpg', 'num': 'shirt89/', 'idx': '89'},
            90:{'title': '雙色印刷條紋短T $614', 'path': '../static/image/b/90.jpg', 'num': 'shirt90/', 'idx': '90'},
            91:{'title': '紐約印花長T $550', 'path': '../static/image/b/91.jpg', 'num': 'shirt91/', 'idx': '91'},
            92:{'title': '混沙緹花毛衣 $390', 'path': '../static/image/b/92.jpg', 'num': 'shirt92/', 'idx': '92'},
            93:{'title': 'BOX厚長T $530', 'path': '../static/image/b/93.jpg', 'num': 'shirt93/', 'idx': '93'},
            94:{'title': '迷彩帽T $730', 'path': '../static/image/b/94.jpg', 'num': 'shirt94/', 'idx': '94'},
            95:{'title': '撞色拼接毛衣 $590', 'path': '../static/image/b/95.jpg', 'num': 'shirt95/', 'idx': '95'},
            96:{'title': '條紋提花毛衣 $695', 'path': '../static/image/b/96.jpg', 'num': 'shirt96/', 'idx': '96'},
            97:{'title': '假兩件長T $298', 'path': '../static/image/b/97.jpg', 'num': 'shirt97/', 'idx': '97'},
            98:{'title': '對抗世界帽T $450', 'path': '../static/image/b/98.jpg', 'num': 'shirt98/', 'idx': '98'},
            99:{'title': '運動線大學服長T $390', 'path': '../static/image/b/99.jpg', 'num': 'shirt99/', 'idx': '99'},
            100:{'title': '鋼印大學服長T $390', 'path': '../static/image/b/100.jpg', 'num': 'shirt100/', 'idx': '100'},
            101:{'title': '落肩假兩件短T $390', 'path': '../static/image/b/101.jpg', 'num': 'shirt101/', 'idx': '101'},
            102:{'title': '漂浮汽水短T $288', 'path': '../static/image/b/102.jpg', 'num': 'shirt102/', 'idx': '102'},
            103:{'title': '最好朋友短T $180', 'path': '../static/image/b/103.jpg', 'num': 'shirt103/', 'idx': '103'},
            104:{'title': '好麻吉短T $219', 'path': '../static/image/b/104.jpg', 'num': 'shirt104/', 'idx': '104'},
            105:{'title': '世界城市短T $238', 'path': '../static/image/b/105.jpg', 'num': 'shirt105/', 'idx': '105'},
            106:{'title': '偷藏比薩短T $199', 'path': '../static/image/b/106.jpg', 'num': 'shirt106/', 'idx': '106'},
            107:{'title': '好時光笑臉短T‧ $336', 'path': '../static/image/b/107.jpg', 'num': 'shirt107/', 'idx': '107'},
            108:{'title': '圓型圖案燙絨短T $417', 'path': '../static/image/b/108.jpg', 'num': 'shirt108/', 'idx': '108'},
            109:{'title': '亮油標語短T $417', 'path': '../static/image/b/109.jpg', 'num': 'shirt109/', 'idx': '109'},
            110:{'title': 'HIGH HOPES短T $340', 'path': '../static/image/b/110.jpg', 'num': 'shirt110/', 'idx': '100'},
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
    randomed=random.sample(range(109),40)
    for idx in range(0, len(randomed)):
        randomed[idx]=randomed[idx]+1

    randomed = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42}
    for key, value in sort_list.items():
        if key in randomed:
            new_d[key] = value
    print(new_d)
    return render_template("/shirts_b/shirts.htm",title = 'Home',list = new_d,classNum = number_list)

@app.route('/shirts_b/<shirt_id>/')
def rught_page_detail(shirt_id):
    if shirt_id == 'but.htm':
        param = []
        #Do SVM
        with open('../../libsvm-3.22/windows/save_variable','r') as f:
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
        model = svm_load_model("../../libsvm-3.22/python/total_scale.model")
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
            if new_la[idx] == 1:
                recommand.append(new_ind[idx])
        print(recommand)
        #Recommandation System 
        number_of_image = 50
        sorted_sim = []
        #load file from disk
        with open ('outfile', 'rb') as fp:
            sorted_sim = pickle.load(fp)
                
        #find the similar image
        rec_clothes = []
        chosen_images = []
        chosen_img = []
        chosen_images=recommand #6
        for k in range(len(chosen_images)):
            chosen_img = chosen_images[k]
            recommand_num = 3 #decide how many images to recommand
            for i in range(recommand_num):
                im_num = sorted_sim[chosen_img][i][1]
                rec_clothes.append(sorted_sim[chosen_img][i][1])
        #print("cloth %d" %chosen_img)
        print(rec_clothes)

        for key, value in sort_list.items():
            if key in rec_clothes:
                new_d[key] = value
        sort_d = collections.OrderedDict(new_d)
        return render_template("/shirts_b/but.htm",title= 'Result', list = sort_d, classNum = number_list)
    else:
        return render_template("/shirts_b/%s/a.htm" %shirt_id)

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
    print(click)


if __name__ == "__main__":
	app.debug=True
	app.run()
