import matplotlib.pyplot as plt

# 1. 배경 및 이미지 크기 설정
fig, ax = plt.subplots(figsize=(7, 2))
fig.patch.set_facecolor('#ffffff') # 전체 배경 흰색
ax.set_facecolor('#ffffff') 

# 2. 텍스트로 깔끔하게 수식 그리기 (% 연산자 사용)
# 에러가 나던 \pmod 대신 직관적인 % 기호로 변경했습니다.
formula = r"$idx = hash(key) \ \% \ self.size$"

# 글자 크기를 키우고 더 깔끔하게 정렬
ax.text(0.5, 0.5, formula, size=24, color='#111111', 
        ha='center', va='center', weight='bold')

# 3. 테두리와 축 완전히 숨기기
ax.axis('off')

# 4. 여백 없이 고화질 이미지 파일로 저장
plt.savefig('hash_formula.png', bbox_inches='tight', pad_inches=0.2, dpi=300)
plt.close()

print("🎉 성공! 에러 없이 'hash_formula.png' 파일이 생성되었습니다!")