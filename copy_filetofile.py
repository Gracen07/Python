def copy_file(src_file, destin_file):
        with open(src_file, 'r') as src:
            with open(destin_file, 'w') as dest:
                for line in src:
                    dest.write(line)
        
        print(f"Contents from {src_file} copied to {destin_file} successfully.")
src_file = 'source.txt' 
destin_file = 'destination.txt'

copy_file(src_file, destin_file)
