//
//
// Pattern Matching
// Outputs character index start counts at 0
//
//

import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.InputStreamReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.File;
import java.util.Scanner;

class patternIndex {
	public static String genome;
	public static void main(String[] args) {
		File genomeFile = new File("genome.txt");
		String pattern = "CTTGATCAT";
		
		if(genomeFile.exists()) {
			genome = genomeString(genomeFile);
		}
		System.out.println(genome);
	}
	
	
}
public class importString {
	public static String genomeString(path) {
		String text = new scanner( new file(path) ).usedelimiter("\\a").next();
		return text;
	}
}