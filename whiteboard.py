# from TextWash.zhonTranslate import CNwash
# CNwash(r"D:\Documents\GitHub\Learning_SQL\SQL101byMick\Chatper_5_Complex_Query.md")


nums = [4,5,5, 4,5,5]
L = len(nums)

small, large = min([nums[:L//2], nums[L//2:]], key=sum), max([nums[:L//2], nums[L//2:]], key=sum)

print(small, large)
