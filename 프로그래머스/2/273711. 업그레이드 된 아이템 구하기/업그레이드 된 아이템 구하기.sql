-- 아이템의 희귀도가 RARE인 아이템들의 다음을 알려고 하는 것.
-- 그래서 부모 아이템 중에 RARE인 것부터 고르고, 부모의 아이디를 갖고 있는 자식(ID)을 TREE 테이블에서 찾는다.
-- 그리고 찾은 TREE테이블에서의 자식 ID랑 같은 ITEM_INFO의 정보(자식 C테이블)를 출력하는 것.

SELECT C.ITEM_ID, C.ITEM_NAME, C.RARITY
FROM ITEM_TREE T, ITEM_INFO C, ITEM_INFO P
WHERE P.RARITY = 'RARE' AND P.ITEM_ID = T.PARENT_ITEM_ID AND T.ITEM_ID = C.ITEM_ID
ORDER BY C.ITEM_ID DESC