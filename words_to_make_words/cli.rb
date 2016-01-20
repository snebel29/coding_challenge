#!/usr/bin/ruby

def validate(source, word)
    word.split("").each do |char|
        if ! source.include?(char)
            puts "The word #{word} is not valid because you can't build it using #{source}"
            exit(1)
        end
    end
end

def how_many_sources?(source, word)

    validate(source, word)
    source_letter_coefficient = {}

    source.split("").each do |char|
        if source_letter_coefficient.include?(char)
            source_letter_coefficient[char] = source_letter_coefficient[char] +1
        else
            source_letter_coefficient[char] = 1
        end
    end

    source_letter_coefficient.each {|c,v| source_letter_coefficient[c] = 1.0 / source_letter_coefficient[c]}
    word_letter_count = {}
    word.split("").each do |char|
        if word_letter_count.include?(char)
            word_letter_count[char] = word_letter_count[char] + source_letter_coefficient[char]
        else
            word_letter_count[char] = source_letter_coefficient[char]
        end
    end

    puts word_letter_count.values.max.ceil
end


if __FILE__ == $0

    if ARGV.length < 2
        puts "Argument count error"
        puts "#{__FILE__} <firstletter> <secondletter>"
        exit(1)
    end

    source = ARGV[0].gsub(' ','') 
    word = ARGV[1].gsub(' ','')

    how_many_sources?(source, word)

end
