### 이동차량 종류 및 개수 파악 알고리즘 

#### 진행과정 
![최종_빅리더AI_NEXTLEVEL_bigchallenge_발표자료_25](https://user-images.githubusercontent.com/67791317/203755214-73003e96-8b95-493b-a638-1714bcadb4ba.jpg)

#### 모델 선정 
![최종_빅리더AI_NEXTLEVEL_bigchallenge_발표자료_26](https://user-images.githubusercontent.com/67791317/203755219-fc413129-eb2c-4753-9620-bc2bf4d3996c.jpg)

YOLO 모델은 영역 검출과 분류를 동시에 함으로써 이미지 파일에서 특정 사물(규칙적으로 학습한 사물, 동물의 형체와 얼굴 등)을 분류할 수 있기 때문에 선정했습니다. 특히 YOLO v5는 지속적으로 성능을 향상 시킴으로서 사진에 적힌 특징을 갖게 되어 사용하게 되었습니다. 

*본 서비스 구현는 사진이 아닌 실시간 동영상에서 차량을 인식해야하기 때문에 Deep Sort 모델을 함께 사용합니다.*

#### 
![최종_빅리더AI_NEXTLEVEL_bigchallenge_발표자료_27](https://user-images.githubusercontent.com/67791317/203755222-026f2a06-0c52-4535-8f8d-2f5804d42b48.jpg)

AI 모델을 사용하여 원하는 알고리즘을 만들기 위해선 양질의 데이터가 꼭 필요하지만 협력 기관의 특성상 이미지 파일 혹은 동영상 파일등의 데이터 일체를 받지 못했습니다. 따라서 최근 6개월 동안 수출되는 차량들의 이미지 파일을 중고차 사이트를 웹 크롤링하여 약 4000여 개의 데이터를 수집했습니다. 

![최종_빅리더AI_NEXTLEVEL_bigchallenge_발표자료_28](https://user-images.githubusercontent.com/67791317/203755227-8fdaceaa-c3f0-4443-ad07-f5a436999070.jpg)

알고리즘 학습에 사용할 수 있도록 라벨링 작업을 수작업 했습니다. 

![최종_빅리더AI_NEXTLEVEL_bigchallenge_발표자료_29](https://user-images.githubusercontent.com/67791317/203755232-64360086-961b-473d-826b-2bc98042bd1d.jpg)

차량 운송 과정에서 얻는 실시간 영상은 기후 혹은 시간에 따라 환경적 요인이 달라집니다. 따라서 조도, 명암, 기울기 그리고 형태 등을 고려하여 1 프레임에 8가지 증강 기법을 사용하여 데이터를 증가 시켰습니다. 

#### 모델 학습

![최종_빅리더AI_NEXTLEVEL_bigchallenge_발표자료_30](https://user-images.githubusercontent.com/67791317/203755236-714c6111-63f5-4963-a743-5b04df870482.jpg)

17개의 차량 종류를 48,156개의 이미지 파일로 학습하여 각각 99%, 97%의 정확도로 분류하는 분류 모델을 완성했습니다. 

#### Deep Sort (추적)

![최종_빅리더AI_NEXTLEVEL_bigchallenge_발표자료_31](https://user-images.githubusercontent.com/67791317/203755240-22c17c8d-2b74-4b8f-9e94-a2f7ca842487.jpg)

그동안 학습시킨 분류 모델은 이미지 파일에서 원하는 차종을 분류하고 카운트하는 모델이었다. 따라서 실시간으로 이동하는 차량이 담긴 동영상을 처리하기 위해 Tracking을 수행할 수 있도록 Deep Sort 모델을 사용했다.   

연속으로 쌓이는 이미지 데이터 분포에서 새로운 분포를 예측함으로 영역을 검출하는 원리로 사용하는 모델이다. 

#### 모델 Test 결과

![최종_빅리더AI_NEXTLEVEL_bigchallenge_발표자료_32](https://user-images.githubusercontent.com/67791317/203755242-20e50863-fd0d-49dc-8a09-1013b4b46957.jpg)