// Name         : Waseem Alkasbutrus
// ID           : 1001849127
// Lang Version : openjdk version "11.0.16" 2022-07-19
// OS           : Ubuntu 20.04.5 LTS (Not on a virtual machine)

// NOTE: Check README.md for answer to questions 1 and 2

import java.io.File;
import java.nio.file.Files;

class wia1927_lab01 {
    public static void main(String[] args) {
        long sum = sumFileSizes(new File("."));
        
        System.out.println(sum);
    }

    public static long sumFileSizes(File dir) {
        long size = 0;

        // get entries of dir
        String[] entries = dir.list();


        // for each object in the current directory
        for (String entryName : entries) {
            File entry = new File(dir.getAbsolutePath() + "/" + entryName);

            // check if it is a file or a directory
            if (entry.isFile() && entryName != "." && entryName != "..") {
                
                // Files.size can throw an exception, so use a try-catch block to catch any thrown exceptions 
                try {
                    // if it is a file, get its size
                    size += Files.size(entry.toPath());
                } catch (Exception e) {
                    System.out.println(e.getMessage());
                }

            } else if (entry.isDirectory() && entryName != "." && entryName != "..") {
                // if it is a dir, call this function again
                size += sumFileSizes(entry);
            }
        }
        
        return size;
    }
}