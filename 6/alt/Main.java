import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.Arrays;
import java.util.HashSet;
import java.util.stream.Collectors;

public class Main {
    static Integer part1(String input){
        return Arrays.stream(input.split("\n\n"))
                .map(
                        (answers) -> Arrays.stream(answers.split("\n"))
                                .map(x -> x.chars().mapToObj(i -> (char)i).collect(Collectors.toSet()))
                                .collect(HashSet::new, HashSet::addAll, HashSet::addAll).size()
                ).mapToInt(Integer::intValue).sum();
    }

    static Integer part2(String input){
        return Arrays.stream(input.split("\n\n"))
                .map(
                        (answers) -> Arrays.stream(answers.split("\n"))
                                .map(x -> x.chars().mapToObj(i -> (char)i).collect(Collectors.toSet()))
                                .collect(() -> new HashSet<>("abcdefjghijklmnopqrstuvwxyz"
                                        .chars()
                                        .mapToObj(e -> (char)e)
                                        .collect(Collectors.toList())
                                ), HashSet::retainAll, HashSet::retainAll).size()
                ).mapToInt(Integer::intValue).sum();
    }

    public static void main(String[] args) {
        File file = new File("6.in");
        String input = "";

        if(file.exists()){
            try {
                input = Files.readString(file.toPath());
            } catch (IOException e){
                e.printStackTrace();
            }
        }

        System.out.println("Part 1: " + part1(input).toString());
        System.out.println("Part 2: " + part2(input).toString());

    }
}
