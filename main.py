import roboskill

@roboskill.skill('asdzxc')
async def main():
  a = 1
  a += 2
  print(a)

if __name__ == '__main__':
  roboskill.run()