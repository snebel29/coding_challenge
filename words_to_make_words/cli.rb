#!/usr/bin/ruby

class Cli

    attr_reader :source, :word, :not_valid__msg
    attr_writer :source, :word 

    def initialize(source, word)
        @source = source
        @word = word
        @not_valid__msg = "The word #{word} is not valid because you can't build it using #{source}"
    end

    def validate
        word.split("").each do |char|
            if ! source.include?(char)
                return false
            end
        end
    end

    def how_many_sources?

        return false if not self.validate
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

        word_letter_count.values.max.ceil
    end
end

if __FILE__ == $0

    if ARGV.length < 2
        puts "Argument count error"
        puts "#{__FILE__} <firstletter> <secondletter>"
        exit(1)
    end

    source = ARGV[0].gsub(' ','') 
    word = ARGV[1].gsub(' ','')

    cli = Cli.new(source, word)
    result = cli.how_many_sources?
    if result then puts result else puts cli.not_valid__msg end

end
