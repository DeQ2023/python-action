import os
def main():
  print("Hellow from Github Actions!")
  token = os.environ.get("AWS_SECRET_TOKEN")
  if not token:
    raise RuntimError("AWA-SECRET_TOKEN env var is not set!")
  print("All good! we found our env var")


if __name__ == '__main__':
  main()
