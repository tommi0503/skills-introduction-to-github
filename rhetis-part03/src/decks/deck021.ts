import type {Deck} from '../model'
import {T,B,P,S,D} from '../primitives'
const navy='#1c3949',pink='#f5aaa2'
const title='SWOT 분석 및 조사\n[ 브랜드네임 ]'
export const deck021:Deck=D('021','폴더링 프레젠테이션',[S('slide_01','SWOT 분석 및 조사',pink,[
B(0,0,16,720,navy),P([[16,200],[40,200],[40,581],[16,625]],'#f7c46f',0,'#f7c46f'),P([[16,180],[40,180],[40,442],[16,480]],'#abc6c4',0,'#abc6c4'),P([[16,160],[40,160],[40,363],[16,404]],'#ead7b9',0,'#ead7b9'),P([[16,140],[40,140],[40,284],[16,328]],'#bb8359',0,'#bb8359'),B(0,0,58,285,navy,{radius:'0 0 42px 0',shadow:'14px 4px 22px #765c4c35'}),P([[0,0],[15,0],[15,29],[20,43],[44,47],[55,55],[58,65],[58,242],[52,269],[16,329],[0,329]],navy,0,navy),P([[1236,720],[1280,720],[1280,201],[1266,227],[1237,272]],'#fff',0,'#fff'),
T(247,149,800,245,title,96,{font:'Pretendard',weight:900,color:navy,align:'center',lineHeight:1.08,letterSpacing:-5,textStroke:`4px ${navy}`}),
T(244,146,800,245,title,96,{font:'Pretendard',weight:900,color:pink,align:'center',lineHeight:1.08,letterSpacing:-5,textStroke:`3px ${pink}`}),
T(241,143,800,245,title,96,{font:'Pretendard',weight:900,color:navy,align:'center',lineHeight:1.08,letterSpacing:-5,textStroke:`1px ${navy}`}),
T(425,402,430,52,'~ BRANDNAME ~',38,{font:'Pretendard',weight:800,letterSpacing:4,color:'#a32e22',align:'center'}),B(583,561,37,37,navy,{radius:'50%'}),T(583,563,37,37,'3',30,{font:'Pretendard',weight:700,color:pink,align:'center'}),T(623,560,49,44,'조',36,{font:'Pretendard',weight:700,color:navy}),T(385,625,510,36,'미리대학교 경영학과 12345678 강미리',24,{font:'Pretendard',weight:700,color:navy,align:'center'})])])
