#!/usr/bin/ruby

require 'test/unit'
require './cli'

class CLi_test < Test::Unit::TestCase
    def test_words
        assert_equal(1, Cli.new('coffeole', 'feo').how_many_sources?)
        assert_equal(2, Cli.new('bookcase', 'bbookcase').how_many_sources?)
        assert_equal(false, Cli.new('window', 'chair').how_many_sources?)
        assert_equal(4, Cli.new('hooola', 'hhhhooolaaooo').how_many_sources?) 
    end
end
