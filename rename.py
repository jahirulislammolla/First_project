import re,os,random,array
path='/home/jahir/Desktop/Videos'
with open(path+"/names.txt") as f:
    content = f.read().splitlines()
    print (content)
    dir,sub_dir,file,i_sub_dir,i_file='','','',0,0
    print (sum([9,8]))
    for i in content:
        if i!="":
            if re.match(r'^[1-4]',i):
                dir="/"+re.sub('[^a-zA-Z]','',i)
                i_sub_dir=1
            elif re.match(r'[a-zA-Z ]+$',i):
                sub_dir=re.sub('[ ]','_',i)
                new_dir=str(i_sub_dir)+"_"+sub_dir
                f_path = path + dir
                #print (new_dir)
                folders = next(os.walk(f_path))[1]
                if sub_dir in folders:
                    os.rename(os.path.join(f_path, sub_dir), os.path.join(f_path, new_dir))
                    sub_dir=new_dir
                i_sub_dir+=1
                i_file=1
            else:
                file=re.sub(r'[^a-zA-Z]','',i)+"MagooshGRE.mp4"
                folders = next(os.walk(path+dir))[1]
                if sub_dir in folders:
                    f_path=path+dir+"/"+sub_dir
                    files=next(os.walk(f_path))[2]
                    new_file=str(i_file)+"_"+file
                    if file in files:
                        os.renames(os.path.join(f_path,file),os.path.join(f_path,new_file))
                    i_file+=1