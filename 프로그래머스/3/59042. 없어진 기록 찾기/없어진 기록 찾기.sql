-- ANIMAL_INS: 동물 보호소에 들어온 동물의 정보
-- 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부

-- ANIMAL_OUTS: 동물 보호소에서 입양 보낸 동물의 정보
-- 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부

SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS O 
LEFT OUTER JOIN ANIMAL_INS I
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.INTAKE_CONDITION IS NULL