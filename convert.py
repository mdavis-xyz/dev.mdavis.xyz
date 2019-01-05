from mako.template import Template
import datetime as dt
import yaml
import pprint as pp
import shutil
from subprocess import call
import pypandoc
import os
import re

template_fname = "template.html"
output_fname = "pages/www/docs/index.html"
pagesFname = 'pages.yaml'
enableTracking = False


# today = dt.date.today()
# date = {
#    'human': today.strftime('%d, %b %Y')
# }

with open(template_fname,"r") as f:
    template = Template(f.read())

def callShellCmd(cmd,directory):
    print("Calling `%s` in %s" % (cmd,directory))
    ret = call(cmd, shell=True, cwd=directory)
    assert(not ret)
    print("Finished calling `%s` in %s" % (cmd,directory))

def stripMarkdown(text):
    expr = r'<[^<>]+>'
    text = re.sub(expr, '', text)
    expr = r'\[([^\[\]]+)\]\(([^\(\)]+)\)'
    text = re.sub(expr, r'\1', text)
    return(text)

def testStripMarkdown():
    original = 'asd'
    expected = 'asd'
    actual = stripMarkdown(original)
    assert(expected == actual)

    original = '1 <a href="123">blah</a> 2'
    expected = '1 blah 2'
    actual = stripMarkdown(original)
    assert(expected == actual)

    original = 'This [link](http://example.com) shows [this](./blah)'
    expected = 'This link shows this'
    actual = stripMarkdown(original)
    if expected != actual:
        print("actual: " + actual)
    assert(expected == actual)

def numWords(markdown):
    content = stripMarkdown(markdown)
    numWords = len([w for w in content.split(' ') if w.strip() != ''])
    print("Number of words is %d" % numWords)
    return(numWords)

def estReadingTime(markdownFname):
    with open(markdownFname,'r') as f:
        markdown = f.read()


    wpm = 265 # https://help.medium.com/hc/en-us/articles/214991667-Read-time
    minutes = numWords(markdown) / float(wpm)
    return(minutes)

def testNumWords():
    text = 'Hi [this](http://blah.com) is <i>a</i> Test!'
    expected = 5
    actual = numWords(text)
    assert(actual == expected)

# data is for just this page
def doOne(data,allData):
    data['template'] = data['template'].lower()
    assert(data['template'] in ['none','custom','markdown','home'])
    if data['template'] == 'none':
        print("Skipping processing for %s" % data['path'])
    else:
        print("Processing %s" % data['title'])


        directory = 'pages/%s' % data['sourcePath']
        if data['template'] == 'home':
            data['content'] = doWWW(allData)
        elif data['template'] == 'custom':
            print("Processing as custom page")
            cmd = 'python %s' % data['parseScript']
            callShellCmd(cmd,directory)
            stubFname = 'pages/%s/stub.html' % data['sourcePath']
            with open(stubFname,"r") as f:
                data['content'] = f.read()
            # print("Estimating reading time for %s" % data['title'])
            # data['estReadingTime'] = estReadingTime(stubFname)
            # if data['path'] == 'govlist':
            #     print("Halving abbott list reading time estimate")
            #     data['estReadingTime'] = data['estReadingTime']/2.0
        elif data['template'] == 'markdown':
            markdownFname = 'pages/%s/%s' % (data['sourcePath'],data['markdown'])
            print("Converting markdown file %s to html " % markdownFname)
            data['content'] = pypandoc.convert_file(markdownFname, 'html')
            stubFname = 'pages/%s/stub.html' % data['path']
            with open(stubFname,'w') as f:
                f.write(data['content'])
            print("Saved markdown file to %s" % stubFname)
            if 'exclude' not in data:
                data['exclude'] = []
            data['exclude'].append('script')
            print("Estimating reading time for %s" % data['title'])
            data['estReadingTime'] = estReadingTime(markdownFname)


        if 'date' in data:
            date = {
                'original': dt.datetime.strptime(data['date'], '%d/%m/%Y').date()
            }
            print("Reading in date as %s" % str(date['original']))
        else:
            date = {
                'original': dt.date.today()
            }
        date['human'] = date['original'].strftime('%d %b %Y').lstrip('0')
        date['computer'] = date['original'].strftime('%Y-%m-%d')
        data['date'] = date
        if 'exclude' not in data:
            data['exclude'] = []
        renderOne(data)

def renderOne(data):

        try:
            assert('title' in data)
            assert('description' in data)
            assert('images' in data)
            assert('card' in data['images'])
            assert('path' in data['images']['card'])
            assert('publishPath' in data)
            assert('sourcePath' in data)
            assert('height' in data['images']['card'])
            assert('width' in data['images']['card'])
            assert('exclude' in data)
            assert('content' in data)
            if 'date' not in data['exclude']:
                assert('date' in data)
                assert('human' in data['date'])
                assert(type(data['date']['human']) == type(''))
                assert('computer' in data['date'])
                assert(type(data['date']['computer']) == type(''))
        except AssertionError as e:
            pp.pprint({k:data[k] for k in data if k != 'content'})
            print("Error with data %s" % data['title'])
            raise(e)
        print("Rendering page %s" % data['title'])
        try:
            output = template.render(data=data,enableTracking=enableTracking)
        except TypeError as e:
            pp.pprint({k:data[k] for k in data if k != 'content'})
            print("Error processing outer template for %s" % data['title'])
            raise(e)
        outputFname = 'pages/%s/docs/index.html' % data['sourcePath']
        with open(outputFname,'w') as f:
            f.write(output)
        print("Finished rendering %s" % data['sourcePath'])

def doWWW(pages):
    print("Processing www")
    wwwTemplateFname = 'pages/www/template.html'
    with open(wwwTemplateFname, 'r') as f:
        wwwTemplate = Template(f.read())
    for page in pages:
        try:
            assert('images' in page)
            assert('card' in page['images'])
            assert('width' in page['images']['card'])
            assert('height' in page['images']['card'])
            assert('path' in page['images']['card'])
            assert('description' in page['images']['card'])
            assert('title' in page)
            assert('description' in page)
        except AssertionError as e:
            pp.pprint(page)
            print("Error with data for page %s" % page['title'])
            raise(e)
    outputHTML = wwwTemplate.render(pages=[p for p in pages if p['template'] != 'home'])

    outputFname = 'pages/www/stub.html'
    with open(outputFname,"w") as f:
        f.write(outputHTML)
    print("Finished processing www")

    return(outputHTML)

def doAll():
    print("Loading in %s" % pagesFname)
    with open(pagesFname,'r') as f:
        pagesData = yaml.load(f)
    pp.pprint(pagesData)

    for page in pagesData:
        if 'path' in page:
            page['publishPath'] = page['path']
            page['sourcePath'] = page['path']
        else:
            assert('publishPath' in page)
            assert('sourcePath' in page)

    for page in pagesData:
        doOne(page,pagesData)



    src = 'pages/www/docs'
    dest = 'docs/'
    print("copying %s to %s" % (src,dest))
    shutil.rmtree(dest,ignore_errors=True)
    # os.makedirs(dest)
    shutil.copytree(src, dest)
    for page in [p for p in pagesData if p['template'] != 'home']:
        src = './pages/%s/docs' % page['sourcePath']
        dest = './docs/%s/' % page['publishPath']
        print("copying %s to %s" % (src,dest))
        shutil.copytree(src, dest)

    print("Done")

def test():
    testStripMarkdown()
    testNumWords()

test()
doAll()